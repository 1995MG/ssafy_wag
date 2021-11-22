<template>
  <div @click="toDetail(movie)" class="card" style="width: 18%;">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body">
      <p class="card-title fw-bold fs-6">{{ movie.title }}</p>
      <p>★ {{ movie.vote_average }}</p>
      <p>{{ movie.release_date | dateParse('YYYY-MM-DD') | dateFormat('YY.MM.DD') }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  data: function () {
    return {
      poster: null,
    }
  },
  props: {
    movie: Object
  },
  methods: {
    toDetail: function (movie) {   
        this.$router.push({ name: 'MovieDetail', params: {movieId: movie.id} })   
    },
  },
  created: function () {
    this.poster = `https://www.themoviedb.org/t/p/w440_and_h660_face/${this.movie.poster_path}`
  }
}
</script>

<style>

</style>