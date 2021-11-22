<template>
  <div class="container my-5">
    <h1 class="fw-bold">영화추천</h1>
    <!-- 랜덤영화추천 -->
    <div class="my-5">
      <div class="d-flex">
        <h3 class="fw-bold">랜덤추천</h3>
        <button @click="getRandom" class="btn btn-success mx-3">돌려돌려</button>
      </div>
        <div class="d-flex justify-content-around mt-3">
          <div @click="toDetail(movie)" class="card" style="width: 18%;"
            v-for="movie in sample" :key="movie.id"
          >
            <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_path}`" class="card-img-top" alt="...">
            <div class="card-body">
              <p class="card-title fw-bold fs-6">{{ movie.title }}</p>
              <p>★ {{ movie.vote_average }}</p>
              <p>{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YYYY') }}</p>
            </div>
          </div>
        </div>
    </div>
    <!-- 알고리즘기반영화추천 -->
    <div class="my-5">
      <h3 class="fw-bold">그루트추천</h3>
      <div class="d-flex justify-content-around mt-3">
          <div @click="toDetail(movie)" class="card" style="width: 18%;"
            v-for="movie in rcmdMovies" :key="movie.id"
          >
            <img :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_path}`" class="card-img-top" alt="Not Found" onerror="this.src='#';" >
            <div class="card-body">
              <p class="card-title fw-bold fs-6">{{ movie.title }}</p>
              <p>★ {{ movie.vote_average }}</p>
              <p>{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YYYY') }}</p>
            </div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import jwt_decode from 'jwt-decode'

export default {
  name: 'Recommend',
  data: function () {
    return {
      movies: [],
      rcmdMovies: [],
      sample: null,
      userId: null,
      movieId: null,
    }
  },
  methods: {
    toDetail: function (movie) {   
        this.$router.push({ name: 'MovieDetail', params: {movieId: movie.id} })   
    },
    getRandom: function () {
      this.sample = _.sampleSize(this.movies, 5)
    },
    getRecommend: function () {
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/recommended/${this.movieId}/`,
        })
          .then((res) => {
            this.rcmdMovies.push(_.flattenDeep(res.data.DirectorMovie))
            this.rcmdMovies.push(_.flattenDeep(res.data.actorMovie))
            this.rcmdMovies.push(_.flattenDeep(res.data.genreMovie))
            this.rcmdMovies = _.sampleSize(_.flattenDeep(this.rcmdMovies), 5)
          })
          .catch((err) => {
            console.log(err)
          })
    },
  },
  created: function () {
    axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/`,
        })
          .then((res) => {
            // console.log(res.data)
            this.movies = res.data
            this.sample = _.sampleSize(this.movies, 5)
          })
          .catch((err) => {
            console.log(err)
          })

    const token = localStorage.getItem('jwt')
    this.userId = jwt_decode(token).user_id
    axios({
      method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.userId}/rank/`,
        // headers: this.getToken()
      })
        .then((res) => {
          this.movieId = res.data.reverse()[0].movie
          console.log(this.movieId)
          this.getRecommend()
        })
        .catch((err) => {
          console.log(err)
        })
  }
}
</script>

<style>

</style>
