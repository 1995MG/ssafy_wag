<template>
  <div class="container my-5">
    <!-- 게시글 정보 -->
    <div class="d-flex justify-content-between">
      <div>
        <h3 class="fw-bold">{{ article.title }}</h3>
        <!-- <p>{{ article.username }}  |  {{ article.created_at.substring(0,10) }} {{ article.created_at.substring(11,16) }}</p> -->
      </div>
      <div class="d-flex align-items-center">
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
      <comment-list></comment-list>
      <!-- 댓글입력 -->
      <comment-form></comment-form>
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
      article: null,
      liked: null
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    like: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${this.article.id}/likes/`,
        headers: this.setToken()
      })
        .then((res) => {
          this.liked = res.data.liked
          console.log(res.data)
        })
        .catch((error) => {
          console.log(error)
        })
      }
  },
  created: function () {
    this.article = this.$route.query.article
    // console.log(this.$route.query)
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/${this.article.id}/likes/`,
      headers: this.setToken()
    })
      .then((res) => {
        this.liked = res.data.liked
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>