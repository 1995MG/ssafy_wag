<template>
  <div class="container my-5 border">
    <div class="row">
      <img class=col-8 :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_path}`" alt="..." style="">
      <!-- 영화정보 -->
      <div class="col-4">
        <h1 class="fw-bold">유튜브</h1>
        <h1 class="fw-bold">{{ movie.title }}</h1>
        <h5 class="fw-bold">{{ movie.overview }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movie: '',
      movieId: null
    }
  },
  created: function () {
    this.movieId = this.$route.params.movieId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movieId}/`,
    })
      .then((res) => {
        console.log(res.data)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>