<template>
  <div class="container my-5">
    <!-- 게시글 정보 -->
    <div>
      <h3 class="fw-bold">스파이더맨 노웨이홈 너무너무너무 기대된다!!</h3>
      <p>작성자 | 작성시간</p>
    </div>
    <hr>
    <!-- 게시글 내용 -->
    <div>
      <p>내용</p>
    </div>
    <hr>
    <!-- 댓글부분 -->
    <div>
      <!-- 댓글내용 -->
      <div>
        <h5 class="fw-bold">댓글</h5>
        <p>댓글내용</p>
      </div>
      <!-- 댓글입력 -->
      <textarea class="form-control" placeholder="댓글을 남겨보세요." rows="5"></textarea>
      <div class="d-flex justify-content-end my-2">
        <button class="btn btn-success">등록</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArticleDetail',
}
</script>

<style>

</style>