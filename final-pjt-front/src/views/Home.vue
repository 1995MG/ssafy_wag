<template>
  <div class="container my-5">
    <h1 class="fw-bold">현재상영작</h1>
    <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
      <input @click="orderByPop" type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
      <label class="btn btn-outline-success" for="btnradio1">인기순</label>
      <input @click="orderByLikes" type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
      <label class="btn btn-outline-success" for="btnradio2">평점순</label>
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
import _ from 'lodash'
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'Home',
  data: function () {
    return {
      originalMovies: null,
      moviesOrder: null,
      movies: null,
      page: 1,
    }
  },
  components: {
    MovieList,
  },
  methods: {
    orderByPop: function () {
      this.page = 1
      this.moviesOrder = _.orderBy(this.originalMovies, 'popularity', 'desc')
      this.movies = _.slice(this.moviesOrder, (this.page-1)*5, this.page*5)
    },
    orderByLikes: function () {
      this.page = 1
      this.moviesOrder = _.orderBy(this.originalMovies, 'vote_average', 'desc')
      this.movies = _.slice(this.moviesOrder, (this.page-1)*5, this.page*5)
      console.log(this.page)
    },
    plusPage: function() {
      if (this.page == 100) {
        this.page = 100
      } else {
        this.page += 1
        this.movies = _.slice(this.moviesOrder, (this.page-1)*5, this.page*5)
      }
    },
    minusPage: function() {
      if (this.page==1) {
        this.page = 1
      } else {
        this.page -= 1
        this.movies = _.slice(this.moviesOrder, (this.page-1)*5, this.page*5)
      }
    },
  },
  created: function () {
    axios({
    method: 'get',
    url: `http://127.0.0.1:8000/movies/`,
    })
      .then((res) => {
        this.originalMovies = res.data
        this.moviesOrder = _.orderBy(res.data, 'popularity', 'desc')
        this.movies = _.slice(this.moviesOrder, (this.page-1)*5, this.page*5)

      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style>

</style>