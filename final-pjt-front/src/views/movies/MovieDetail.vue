<template>
  <div class="container my-5 border">
    <div class="row">
      <img class=col-7 :src="`https://www.themoviedb.org/t/p/w440_and_h660_face/${movie.poster_path}`" alt="..." style="">
      <!-- 영화정보 -->
      <div class="col-5">
        <div class="video-container">
          <iframe class="video-iframe" width="100%" height="300" :src="`https://www.youtube-nocookie.com/embed/${this.youtubeurl}`" frameborder="0" allowfullscreen></iframe>
        </div>
        <div class="my-3">
          <h1 class="fw-bold">{{ movie.title }}</h1>
          <h5 class="">{{ movie.overview }}</h5>
          <hr>
        </div>
        <div>
          <rank-list :movieId="movieId"></rank-list>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RankList from '@/components/RankList.vue'

export default {
  name: 'MovieDetail',
  components: {
    RankList
  },
  data: function () {
    return {
      movie: '',
      movieId: null,
      youtubeurl: null,
    }
  },
  methods: {
    getYoutubeUrl: function () {
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/movie/${this.movieId}/videos?api_key=131783423dfc5d2cb752bba2d8da456e&language=ko`,
      })
        .then((res) => {
          this.youtubeurl = res.data.results[res.data.results.length-1].key
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.movieId = this.$route.params.movieId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${this.movieId}/`,
    })
      .then((res) => {
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    this.getYoutubeUrl()
  }
}
</script>

<style>

</style>