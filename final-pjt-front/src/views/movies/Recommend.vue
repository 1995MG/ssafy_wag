<template>
  <div class="container my-5">
    <h1 class="fw-bold">영화추천</h1>
    <!-- 랜덤영화추천 -->
    <div class="my-5">
      <h3 class="fw-bold">랜덤추천</h3>
        <div class="d-flex justify-content-around">
          <div class="card" style="width: 18%;"
            v-for="movie in movies" :key="movie.id"
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
      <h3>그루트추천</h3>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'Recommend',
  data: function () {
    return {
      movies: [],
    }
  },
  methods: {
    getRandom: function () {
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/movies/`,
        })
          .then((res) => {
            // console.log(res.data)
            this.movies = _.sampleSize(res.data, 5)
          })
          .catch((err) => {
            console.log(err)
          })
    }
  },
  created: function () {
    this.getRandom()
  }
}
</script>

<style>

</style>