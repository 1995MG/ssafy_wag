<template>
  <div class="container my-5">
    <div class="d-flex mb-3">
      <input class="form-control" v-model="keyword" type="text" @keyup.enter="toSearch(keyword)">
      <button class="btn btn-success mx-3" @click="toSearch(keyword)">search</button>
    </div>
    <hr class="text-white">
    <!-- 현재상영작 -->
    <div class="my-4">
      <h1 class="fw-bold text-white">현재상영작</h1>
      <div id="carouselExampleControls" class="my-3 carousel slide d-flex align-items-center" data-bs-ride="carousel">
        <button @click="minusPageNows" class="btn btn-outline-light" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span aria-hidden="true"></span>
          <span>≪</span>
        </button>
        <div class="carousel-inner">
          <movie-list :movies="nows"></movie-list>
        </div>
        <button @click="plusPageNows" class="btn btn-outline-light" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span aria-hidden="true"></span>
          <span>≫</span>
        </button>
      </div>
    </div>
    <hr class="text-white">
    <!-- 영화리스트 -->
    <div class="my-4">
      <div class="d-flex align-items-center">
        <h1 class="fw-bold text-white align-middle mb-0">영화리스트</h1>
        <div class="btn-group mx-3" role="group" aria-label="Basic radio toggle button group">
          <input @click="orderedByPop" type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
          <label class="btn btn-outline-success" for="btnradio1">인기순</label>
          <input @click="orderedByLikes" type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
          <label class="btn btn-outline-success" for="btnradio2">평점순</label>
        </div>
      </div>
      <div class="my-3">
        <div id="carouselExampleControls" class="my-3 carousel slide d-flex align-items-center" data-bs-ride="carousel">
          <button @click="minusPageMovies" class="btn btn-outline-light" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
            <span aria-hidden="true"></span>
            <span>≪</span>
          </button>
          <div class="carousel-inner">
            <movie-list :movies="movies"></movie-list>
          </div>
          <button @click="plusPageMovies" class="btn btn-outline-light" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
            <span aria-hidden="true"></span>
            <span>≫</span>
          </button>
        </div>
        <div class="my-5">
      </div>
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
      originalNows: null,
      moviesOrdered: null,
      nowsOrdered: null,
      movies: null,
      nows: null,
      pageMovies: 1,
      pageNows: 1,
      keyword: null,
    }
  },
  components: {
    MovieList,
  },
  methods: {
    orderedByPop: function () {
      this.pageMovies = 1
      this.moviesOrdered = _.orderBy(this.originalMovies, 'popularity', 'desc')
      this.movies = _.slice(this.moviesOrdered, (this.pageMovies-1)*5, this.pageMovies*5)
    },
    orderedByLikes: function () {
      this.pageMovies = 1
      this.moviesOrdered = _.orderBy(this.originalMovies, 'vote_average', 'desc')
      this.movies = _.slice(this.moviesOrdered, (this.pageMovies-1)*5, this.pageMovies*5)
      console.log(this.pageMovies)
    },
    plusPageMovies: function() {
      if (this.pageMovies == 100) {
        this.pageMovies = 100
      } else {
        this.pageMovies += 1
        this.movies = _.slice(this.moviesOrdered, (this.pageMovies-1)*5, this.pageMovies*5)
      }
    },
    minusPageMovies: function() {
      if (this.pageMovies==1) {
        this.pageMovies = 1
      } else {
        this.pageMovies -= 1
        this.movies = _.slice(this.moviesOrdered, (this.pageMovies-1)*5, this.pageMovies*5)
      }
    },
    plusPageNows: function() {
      if (this.pageNows == 4) {
        this.pageNows = 4
        } else {
        this.pageNows += 1
        this.nows = _.slice(this.nowsOrdered, (this.pageNows-1)*5, this.pageNows*5)
      }
    },
    minusPageNows: function() {
      if (this.pageNows==1) {
        this.pageNows = 1
      } else {
        this.pageNows -= 1
        this.nows = _.slice(this.nowsOrdered, (this.pageNows-1)*5, this.pageNows*5)
      }
    },
    toSearch: function (keyword) {
      if (keyword != null) {
        this.$router.push({ name: 'Search', params: {keyword: keyword} })  
      }
    }
  },
  created: function () {
    axios({
    method: 'get',
    url: `http://127.0.0.1:8000/movies/`,
    })
      .then((res) => {
        this.originalMovies = res.data
        this.moviesOrdered = _.orderBy(res.data, 'popularity', 'desc')
        this.movies = _.slice(this.moviesOrdered, (this.pageMovies-1)*5, this.pageMovies*5)

      })
      .catch((err) => {
        console.log(err)
      })
    axios({
    method: 'get',
    url: `https://api.themoviedb.org/3/movie/now_playing?api_key=131783423dfc5d2cb752bba2d8da456e&language=ko-KR&page=1`,
    })
      .then((res) => {
        this.originalNows = res.data.results
        this.nowsOrdered = this.originalNows
        this.nows = _.slice(this.nowsOrdered, (this.pageNows-1)*5, this.pageNows*5)

      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style>

</style>