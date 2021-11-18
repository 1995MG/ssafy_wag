<template>
  <div class="articlelist container">
    <table class="table">
      <thead>
        <tr>
          <th class="text-center" scope="col" style="width: 10%">번호</th>
          <th class="text-center" scope="col" style="width: 50%">제목</th>
          <th scope="col" style="width: 15%">작성자</th>
          <th class="text-center" scope="col" style="width: 15%">작성일</th>
          <th class="text-center" scope="col" style="width: 10%">좋아요</th>
        </tr>
      </thead>  
      <tbody>
        <article-list-item
          v-for="article in articles"
          :key="article.id"
          :article="article"
        >
        </article-list-item>
      </tbody>
    </table>
  </div>
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'

export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },
  props: {
    articles: Array
  }

}
</script>

<style>

</style>