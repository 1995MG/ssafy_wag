<template>
  <div class="container my-5" v-if="article">
    <!-- 게시글 정보 -->
    <div class="d-flex justify-content-between">
      <div>
        <h3 class="fw-bold">{{ article.title}}</h3>
        <p>{{ article.username }}  |  {{ article.created_at }}</p>
      </div>
      <div class="d-flex align-items-center">
        <div v-if="login_user === write_user">
          <button @click="updateArticle(articleId)" class="btn mx-1" style="background-color: lightgray;">수정</button>
          <button @click="deleteArticle" class="btn mx-1" style="background-color: lightgray;">삭제</button>
        </div>
        <span v-if="liked">
          <i @click="like" class="fas fa-heart fa-2x" style="color: red"></i>
        </span>
        <span v-else>
          <i @click="like" class="far fa-heart fa-2x" ></i>
        </span>
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
      <comment-list :articleId="articleId"></comment-list>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import CommentList from '@/components/CommentList.vue'

export default {
  name: 'ArticleDetail',
  components: {
    CommentList,
  },
  data: function () {
    return {
      login_user: null,
      write_user: null,
      article: null,
      liked: null,
      articleId: null
    }
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      this.login_user = jwt_decode(token).user_id
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    like: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${this.articleId}/likes/`,
        headers: this.getToken()
      })
        .then((res) => {
          this.liked = res.data.liked
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
      },
    deleteArticle: function (article) {
      const config = this.getToken()
      // console.log(article)
      axios.delete(`http://127.0.0.1:8000/community/${this.articleId}/`, config)
        .then((res) => {
          console.log(res)
          console.log(article.pk)
          this.$router.push({name:'Community'})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateArticle: function (articleId) {
      console.log(articleId)
      this.$router.push({name: 'ArticleUpdateForm', params: {articleId: articleId}})
    }
  },
  created: function () {
    this.articleId = this.$route.params.articleId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/${this.articleId}/likes/`,
      headers: this.getToken()
    })
      .then((res) => {
        this.liked = res.data.liked
      })
      .catch((error) => {
        console.log(error)
      })
    // console.log(this.$route.params.articleId)
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/${this.articleId}/`,
        // headers: this.getToken()
    })
      .then((res) => {
        this.article = res.data
        this.write_user = this.article.user
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style>

</style>