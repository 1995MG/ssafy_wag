<template>
  <div class="container my-5">
    <!-- 랜덤영화추천 -->
    <div v-if="sample" class="my-3">
      <div class="d-flex">
        <h1 class="fw-bold text-white mb-0">랜덤추천</h1>
        <button @click="getRandom" class="btn btn-sm btn-success my-2 mx-3">돌려돌려</button>
      </div>
        <div class="d-flex justify-content-around mt-3">
          <div @click="toDetail(movie)" class="card text-white" style="width: 18%; height: 485px; background-color: rgba(50, 60, 65, 0.9)"
            v-for="movie in sample" :key="movie.id"
          >
            <img v-if="movie.poster_path" :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_path}`" class="card-img-top" alt="...">
            <img v-else src="@/assets/sadgroot.jpg" height="67%" alt="">
            <div class="card-body d-flex align-items-start flex-column">
              <p class="card-title fw-bold fs-6 mb-auto">{{ movie.title }}</p>
              <p class="my-0 align-text-bottom">{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YYYY') }}</p>
              <p class="my-0 align-text-bottom">★ {{ movie.vote_average }}</p>
            </div>
          </div>
        </div>
    </div>
    <!-- 알고리즘기반영화추천 -->
    <h1 class="fw-bold text-white my-5">그루트추천<b-button class="mx-3 mb-2" v-b-popover.hover.right="'가장 최근 작성한 리뷰의 주연, 감독, 장르를 기반으로 영화를 추천합니다.'">?</b-button></h1>
    <div v-if="rcmdMovies.length" class="">
      <div class="d-flex justify-content-around mt-3">
          <div @click="toDetail(movie)" class="card text-white" style="width: 18%; height: 485px; background-color: rgba(50, 60, 65, 0.9)"
            v-for="movie in rcmdMovies" :key="movie.id"
          >
            <img v-if="movie.poster_path" :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_path}`" class="card-img-top" alt="Not Found" onerror="this.src='#';" >
            <img v-else src="@/assets/sadgroot.jpg" height="72%" alt="">
            <div class="card-body d-flex align-items-start flex-column">
              <p class="card-title fw-bold fs-6 mb-auto">{{ movie.title }}</p>
              <p class="my-0 align-text-bottom" v-if="movie.release_date">{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YYYY') }}</p>
              <p class="my-0 align-text-bottom">★ {{ movie.vote_average }}</p>
            </div>
          </div>
        </div>
    </div>
    <div v-else class="d-flex justify-content-center">
      <h3 class="fw-bold text-white">리뷰를 작성해주세요.</h3>
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
    getDescription: function () {
      alert('hi')
    },
    getRecommend: function () {
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/recommended/${this.movieId}/`,
        })
          .then((res) => {
            console.log(res.data)
            this.rcmdMovies.push(_.flattenDeep(res.data.directorMovie))
            this.rcmdMovies.push(_.flattenDeep(res.data.actorMovie))
            this.rcmdMovies.push(_.flattenDeep(res.data.genreMovie))
            console.log(this.rcmdMovies)
            this.rcmdMovies = _.sampleSize(_.uniq(_.flattenDeep(this.rcmdMovies)), 5)
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
