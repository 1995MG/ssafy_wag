<template>
  <div class="my-3">
    <div class="d-flex justify-content-between">
    <!-- 평점정보 -->
      <div class="d-flex align-items-center">
        <div class="d-flex">
          <h3 class="fw-bold pt-3">{{ rank.score }}</h3>
          <div class="mx-3">
            <h5>{{ rank.content }}</h5>
            <p>{{ rank.username }}</p>
          </div>
        </div>
      </div>
      <div class="d-flex align-items-center">
        <button v-if="login_user === write_user" @click="deleteRank()" class="btn btn-outline-danger btn-sm mx-3">삭제</button>
        <div class="mx-2 pt-3">
          <span v-if="liked">
            <i @click="like" class="fas fa-heart" style="color: red"></i>
          </span>
          <span v-else>
            <i @click="like" class="far fa-heart" ></i>
          </span>
          <p class="text-center">{{ likeCount }}</p>
        </div>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
export default {
  name: 'RankListItem',
  props: {
    ranks: Array,
    rank: Object
  },
  data: function () {
    return {
      login_user: null,
      write_user: null,
      movieId: null,
      idx: null,
      liked: null,
      likeCount: 0,
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      if (token) {

        this.login_user = jwt_decode(token).user_id
        const config = {
          Authorization: `JWT ${token}`
        }
        return config
      }
    },
    like: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movieId}/rank/${this.rank.id}/likes/`,
        headers: this.getToken()
      })
        .then((res) => {
          this.liked = res.data.liked
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    deleteRank: function () {
      this.articleId = this.$route.params.movieId
      axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/movies/${this.movieId}/rank/${this.rank.id}/`,
      headers: this.getToken()
      })
        .then((res) => {
          console.log(res)
          // console.log(rank.id)
          this.idx = this.ranks.indexOf(this.rank)
          this.ranks.splice(this.idx, 1)
          // console.log(this.ranks)
          // console.log(this.rank)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getToken()
    this.write_user = this.rank.user
    this.movieId = this.$route.params.movieId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movieId}/rank/${this.rank.id}/likes/`,
      headers: this.getToken()
    })
      .then((res) => {
        this.liked = res.data.liked
        this.likeCount = res.data.count
      })
      .catch((error) => {
        console.log(error)
      })
  },
  updated: function () {
    this.movieId = this.$route.params.movieId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movieId}/rank/${this.rank.id}/likes/`,
      headers: this.getToken()
    })
      .then((res) => {
        this.liked = res.data.liked
        this.likeCount = res.data.count
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>