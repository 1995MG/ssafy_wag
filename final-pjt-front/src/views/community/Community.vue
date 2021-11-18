<template>
  <div class="community container my-5">
    <div class="d-flex justify-content-between">
      <h1 class="fw-bold">커뮤니티</h1>
      <router-link :to="{ name: 'ArticleForm' }">
        <button class="btn btn-success btn-lg">글쓰기</button>
      </router-link>
    </div>
    <hr>
    <!-- 커뮤니티 페이지 -->
    <div>
      <article-list></article-list>
    </div>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'Community',
  components: {
    ArticleList,
  },
}
</script>

<style>

</style>