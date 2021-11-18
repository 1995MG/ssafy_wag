<template>
  <div class="community container my-5">
    <div class="d-flex justify-content-between">
      <h1 class="fw-bold">커뮤니티</h1>
      <router-link :to="{ name: 'ArticleForm' }">
        <button class="btn btn-success btn-lg">글쓰기</button>
      </router-link>
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
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'Community',
  data: function () {
    return {
      articles: null,
    }
  },
  components: {
    ArticleList,
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
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