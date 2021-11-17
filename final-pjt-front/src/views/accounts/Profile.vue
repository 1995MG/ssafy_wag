<template>
  <div class="container">
    <!-- 프로필 정보 -->
    <div class="row my-5">
      <div class="col-3 d-flex justify-content-center">
        <img src="@/assets/logo.png" alt="">
      </div>
      <div class="col-9 row">
        <div class="d-flex align-items-center">
          <h1 class="fw-bold">이름</h1>
        </div>
        <div class="fw-bold d-flex align-items-center">
          <h1 class="fw-bold">평점</h1>
        </div>
      </div>
    </div>
    <hr>
    <!-- 활동 목록 -->
    <div class="nav my-5">
      <h1>한줄평</h1>
      <h1>게시글</h1>
      <h1>댓글</h1>
    </div>
    <!-- 활동 내역 -->
    <div>
      <h3>리스트</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  components: {

  }
}
</script>

<style>

</style>