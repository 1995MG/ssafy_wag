<template>
  <div>
    <div class="d-flex justify-content-between">
      <div>
        <p class="fw-bold">{{ comment.username }}</p>
        <p>{{ comment.content }}</p>
        <span v-if="liked">
          <i @click="like" class="fas fa-heart fa-2x" style="color: red"></i>
        </span>
        <span v-else>
          <i @click="like" class="far fa-heart fa-2x" ></i>
        </span>
      </div>
      <div class="d-flex align-items-center" v-if="login_user === write_user">
        <button @click="deleteComment" class="btn btn-outline-danger btn-sm">삭제</button>
      </div>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
export default {
  name: 'CommentListItem',
  data: function () {
    return {
      login_user: null,
      write_user: null,
      articleId: null,
      idx: null,
      liked: null,
      likeCount: null
    }
  },
  props: {
    comments: Array,
    comment: Object
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
        url: `http://127.0.0.1:8000/community/${this.articleId}/comment/${this.comment.id}/likes/`,
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
    deleteComment: function (comment) {
      this.articleId = this.$route.params.articleId
      const config = this.getToken()
      axios.delete(`http://127.0.0.1:8000/community/${this.articleId}/comment/${this.comment.id}/`, config)
        .then((res) => {
          console.log(res)
          console.log(comment.id)
          this.idx = this.comments.indexOf(this.comment)
          this.comments.splice(this.idx, 1)
          // console.log(this.comments)
          // console.log(this.comment)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getToken()
    this.write_user = this.comment.user
    this.articleId = this.$route.params.articleId
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/${this.articleId}/comment/${this.comment.id}/likes/`,
      headers: this.getToken()
    })
      .then((res) => {
        this.liked = res.data.liked
        this.likeCount = res.data.count
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>