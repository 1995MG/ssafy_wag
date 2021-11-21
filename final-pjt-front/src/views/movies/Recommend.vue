<template>
  <div class="container my-5">
    <h1 class="fw-bold">영화추천</h1>
    <!-- 랜덤영화추천 -->
    <div class="my-5">
      <h3 class="fw-bold">랜덤추천</h3>
      <div class="d-flex justify-content-around">
        <div class="card" style="width: 18%;">
          <img src="https://www.themoviedb.org/t/p/w440_and_h660_face/aNtAP8ZzUMdnCPoqYgVOcgI0Eh4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title fw-bold">제목</h5>
          </div>
        </div>
        <div class="card" style="width: 18%;">
          <img src="https://www.themoviedb.org/t/p/w440_and_h660_face/aNtAP8ZzUMdnCPoqYgVOcgI0Eh4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title fw-bold">제목</h5>
          </div>
        </div>
        <div class="card" style="width: 18%;">
          <img src="https://www.themoviedb.org/t/p/w440_and_h660_face/aNtAP8ZzUMdnCPoqYgVOcgI0Eh4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title fw-bold">제목</h5>
          </div>
        </div>
        <div class="card" style="width: 18%;">
          <img src="https://www.themoviedb.org/t/p/w440_and_h660_face/aNtAP8ZzUMdnCPoqYgVOcgI0Eh4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title fw-bold">제목</h5>
          </div>
        </div>
        <div class="card" style="width: 18%;">
          <img src="https://www.themoviedb.org/t/p/w440_and_h660_face/aNtAP8ZzUMdnCPoqYgVOcgI0Eh4.jpg" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title fw-bold">제목</h5>
          </div>
        </div>
      </div>
    </div>
    <!-- 알고리즘기반영화추천 -->
    <div class="my-5">
      <h3>그루트추천</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Recommend',
}
</script>

<style>

</style>