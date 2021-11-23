<template>
  <div>
    <movie-list :movies="movies"></movie-list>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'Search',
  data: function () {
    return {
      keyword: null,
      movies: null,
    }
  },
  components: {
    MovieList,
  },
  created: function () {
    this.keyword = this.$route.params.keyword
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/search/${this.keyword}/`,
    })
      .then((res) => {
        console.log(this.keyword)
        this.movies = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
}
</script>

<style>

</style>