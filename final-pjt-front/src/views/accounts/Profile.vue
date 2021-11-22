<template>
  <div class="profile container">
    <!-- 프로필 정보 -->
    <div class="row my-5">
      <div class="col-3 d-flex justify-content-center">
        <img src="@/assets/logo.png" alt="">
      </div>
      <div class="col-9 row">
        <div class="d-flex align-items-center">
          <h1 class="fw-bold">{{ this.username }}</h1>
        </div>
        <div class="fw-bold d-flex align-items-center">
          <h1 class="fw-bold">평점 평균 : {{ this.avg }}</h1>
        </div>
      </div>
    </div>
    <hr>
    <!-- 활동 목록 -->
    <div class="btn-group my-3" role="group" aria-label="Basic radio toggle button group">
      <input @click="getRank" type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
      <label class="btn btn-lg btn-outline-success" for="btnradio1">평점</label>
      <input @click="getArticle" type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
      <label class="btn btn-lg btn-outline-success" for="btnradio2">게시글</label>
      <input @click="getComment" type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
      <label class="btn btn-lg btn-outline-success" for="btnradio3">댓글</label>
    </div>
    <!-- 활동 내역 -->
    <div @click="toDetail(writing)" v-for="writing in writings" :key="writing.id">
      <div v-if="btn==1">
        <h3>{{ writing.title }}</h3>
        <p>{{ writing.created_at}}</p>
      </div>
      <div v-else>
        <h3>{{ writing.content }}</h3>
        <p>{{ writing.created_at }}</p>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import jwt_decode from 'jwt-decode'

export default {
  name: 'Profile',
  data: function () {
    return {
      btn: 0,
      userId: null,
      username: null,
      writings: [],
      avg: null,
      // writing: null,
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getRank: function () {
      this.btn = 0
      axios({
      method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.userId}/rank/`,
        // headers: this.getToken()
      })
        .then((res) => {
          console.log(res.data)
          this.writings = res.data
          this.writings.reverse()
          this.avg = _.meanBy(this.writings, 'score')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getArticle: function () {
      this.btn = 1
      axios({
      method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.userId}/article/`,
        // headers: this.getToken()
      })
        .then((res) => {
          console.log(res.data)
          this.writings = res.data
          this.writings.reverse()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getComment: function () {
      this.btn = 2
      axios({
      method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.userId}/comment/`,
        // headers: this.getToken()
      })
        .then((res) => {
          console.log(res.data)
          this.writings = res.data
          this.writings.reverse()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    toDetail: function (writing) {
      if (this.btn == 0) {
        this.$router.push({ name: 'MovieDetail', params: {movieId: writing.movie} })
      }
      else if (this.btn == 1) {
        this.$router.push({ name: 'ArticleDetail', params: {articleId: writing.id} })
      } else {
        this.$router.push({ name: 'ArticleDetail', params: {articleId: writing.article} })
      }
    }
  },
  created: function() {
    const token = localStorage.getItem('jwt')
    this.userId = jwt_decode(token).user_id

    axios({
      method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.userId}/`,
        headers: this.getToken()
      })
        .then((res) => {
          this.username = res.data.first_name
        })
        .catch((err) => {
          console.log(err)
        })
    
    this.getRank()
  }
}
</script>

<style>

</style>