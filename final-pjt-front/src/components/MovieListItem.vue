<template>
  <div class="card" style="width: 18%;">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title fw-bold">{{ movie.title }}</h5>
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
  created: function () {
    this.poster = `https://www.themoviedb.org/t/p/w440_and_h660_face/${this.movie.poster_path}`
  }
}
</script>

<style>

</style>