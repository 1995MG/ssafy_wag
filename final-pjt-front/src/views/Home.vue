<template>
  <div class="container my-5">
    <h1 class="fw-bold">현재상영작</h1>
    <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
      <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
      <label class="btn btn-outline-primary" for="btnradio1">인기순</label>
      <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
      <label class="btn btn-outline-primary" for="btnradio2">평점순</label>
    </div>
    <div class="my-5">
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <movie-list :movies="movies"></movie-list>
        </div>
        <button @click="minusPage" class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span class="" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
        <button @click="plusPage" class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span class="" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from "lodash"
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'Home',
  data: function () {
    return {
      movies: null,
      page: 1
    }
  },
  components: {
    MovieList,
  },
  methods: {
    getMovies: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/page/${this.page}/`,
      })
        .then((res) => {
          // console.log(res.data)
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // orderByLikes: fucntion() {
    //   this.movies = _.orderBy(this.movies, 'this.movies.vote_average', 'desc')
    // },
    plusPage: function() {
      if (this.page==100) {
        this.page = 100
      } else {
        this.page += 1
      }
      this.getMovies()
    },
    minusPage: function() {
      if (this.page==1) {
        this.page = 1
      } else {
        this.page -= 1
      }
      this.getMovies()
    },
  },
  created: function () {
    this.getMovies()
  },
}
</script>

<style>

</style>