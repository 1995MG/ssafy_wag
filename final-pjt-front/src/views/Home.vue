<template>
  <div class="container my-5">
    <h1 class="fw-bold">HOME</h1>
    <div class="my-5">
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <movie-list></movie-list>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span class="" aria-hidden="true">+</span>
          <span class="visually-hidden">Next</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span class="" aria-hidden="true">+</span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
export default {
  name: 'Home',
  components: {
    MovieList,
  }
}
</script>

<style>

</style>