<template>
  <div class="container my-5">
    <!-- 게시글 정보 -->
    <div class="d-flex justify-content-between">
      <div>
        <h3 class="fw-bold">스파이더맨 노웨이홈 너무너무너무 기대된다!!</h3>
        <p>작성자 | 작성시간</p>
      </div>
      <div class="d-flex align-items-center">
        <i class="far fa-heart fa-2x"></i>
      </div>
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
      <comment-list></comment-list>
      <!-- 댓글입력 -->
      <comment-form></comment-form>
    </div>
  </div>
</template>

<script>
import CommentForm from '@/components/CommentForm.vue'
import CommentList from '@/components/CommentList.vue'

export default {
  name: 'ArticleDetail',
  components: {
    CommentForm,
    CommentList,
  }
}
</script>

<style>

</style>