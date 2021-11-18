<template>
  <div class="container my-5">
    <!-- 게시글 정보 -->
    <div class="d-flex justify-content-between">
      <div>
        <h3 class="fw-bold">{{ article.title}}</h3>
        <p>{{ article.username }}  |  {{ article.created_at.substring(0,10) }} {{ article.created_at.substring(11,16) }}</p>
      </div>
      <div class="d-flex align-items-center">
        <i class="far fa-heart fa-2x"></i>
      </div>
    </div>
    <hr>
    <!-- 게시글 내용 -->
    <div>
      <p>{{ article.content }}</p>
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
  },
  data: function () {
    return {
      article: null
    }
  },
  created: function () {
    this.article = this.$route.query.article
    console.log(this.$route.query)
  }
}
</script>

<style>

</style>