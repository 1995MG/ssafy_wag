<template>
  <div class="container my-5" v-if="article">
    <!-- 게시글 정보 -->
    <div class="d-flex justify-content-between">
      <div>
        <h3 class="fw-bold">{{ article.title}}</h3>
        <p>{{ article.username }}  |  {{ article.created_at }}</p>
      </div>
      <div class="d-flex align-items-center">
        <button @click="updateArticle(article)" class="btn mx-1" style="background-color: lightgray;">수정</button>
        <button @click="deleteArticle" class="btn mx-1" style="background-color: lightgray;">삭제</button>
        <i class="mx-1 far fa-heart fa-2x"></i>
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
      <comment-form :article="article"></comment-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
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
    // console.log(this.$route.params.articleId)
    const articleId = this.$route.params.articleId
    axios({
      method: 'get',
        url: `http://127.0.0.1:8000/community/${articleId}/`,
        // headers: this.getToken()
      })
        .then((res) => {
          // console.log(res)
          this.article = res.data
          console.log(this.article)
        })
        .catch((err) => {
          console.log(err)
        })
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    deleteArticle: function (article) {
      const config = this.getToken()
      // console.log(article)
      axios.delete(`http://127.0.0.1:8000/community/${this.article.id}/`, config)
        .then(res => {
          console.log(res)
          console.log(article.pk)
          this.$router.push({name:'Community'})
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateArticle: function (article) {
      console.log(article)
      this.$router.push({name: 'ArticleUpdateForm', query: {article: article}})
    }
  }
}
</script>

<style>

</style>