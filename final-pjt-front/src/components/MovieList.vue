<template>
  <div class="carousel-item active">
    <div class="d-flex justify-content-around">
      <movie-list-item
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      >
      </movie-list-item>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  props: {
    movies: Array
  },
  
}
</script>

<style>

</style>