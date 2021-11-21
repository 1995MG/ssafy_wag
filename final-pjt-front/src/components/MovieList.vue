<template>
  <div class="carousel-item active">
    <div class="d-flex justify-content-around">
      <movie-list-item></movie-list-item>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'
export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  }
}
</script>

<style>

</style>