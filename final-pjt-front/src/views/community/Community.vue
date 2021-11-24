<template>
  <div class="community container my-5">
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <div class="btn-group mx-3" role="group" aria-label="Basic radio toggle button group">
          <input @click="orderByDate" type="radio" class="btn-check d-flex" name="btnradio" id="btnradio1" autocomplete="off" checked>
          <label class="btn btn-outline-success" style="padding-top: 0.6rem" for="btnradio1">최신순</label>
          <input @click="orderByLike" type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
          <label class="btn btn-outline-success" style="padding-top: 0.6rem" for="btnradio2">좋아요순</label>
        </div>
      </div>
      <div class="d-flex">
        <div class="d-flex">
          <input class="form-control me-1" style="width: 80%" v-model="keyword" type="text" @keyup.enter="toSearch(keyword)">
          <button class="btn btn-success me-3" @click="toSearch(keyword)">search</button>
        </div>
        <router-link :to="{ name: 'ArticleForm' }">
          <button v-if="validtoken" class="btn btn-success btn-lg">글쓰기</button>
        </router-link>
      </div>
    </div>
    <hr>
    <!-- 커뮤니티 페이지 -->
    <div>
      <article-list :articles="articles"></article-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'Community',
  data: function () {
    return {
      validtoken: null,
      articles: null,
      chunkArticle: null,
      keyword: null,
    }
  },
  components: {
    ArticleList,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      this.validtoken = token
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    toSearch: function () {
      if (this.keyword) {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/community/search/${this.keyword}/`,
        })
          .then((res) => {
            this.articles = res.data.reverse()
          })
          .catch((err) => {
            console.log(err)
          })
      } else {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/community/`,
          })
          .then((res) => {
            console.log(this.keyword)
            this.articles = res.data.reverse()
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
    orderByDate: function () {
      this.articles = _.orderBy(this.articles, 'id', 'desc')
    },
    orderByLike: function () {
      this.articles = _.orderBy(this.articles, function (_) {return _.like_users.length}, 'desc')
    },
    getArticles: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/community/',
        headers: this.setToken()
      })
        .then((res) => {
          // console.log(res.data)
          this.articles = res.data
          this.articles.reverse()
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created: function () {
    this.getArticles()
  },
}
</script>

<style>

</style>