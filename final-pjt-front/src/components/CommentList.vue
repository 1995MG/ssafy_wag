<template>
  <div>
    <h5 class="fw-bold my-4">댓글</h5>
    <comment-list-item class="container"
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      :comments="comments"
    >
    </comment-list-item>
    <textarea v-model="content" class="form-control" placeholder="댓글을 남겨보세요." rows="5"></textarea>
    <div class="d-flex justify-content-end my-2">
      <button @click="createComment" class="btn btn-success">등록</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import CommentListItem from '@/components/CommentListItem.vue'

export default {
  name: 'CommentList',
  data: function () {
    return {
      comments: [],
      comment: null,
      content: null,
      user: null,
      username: null,
    }
  },
  props: {
    articleId: [String, Number],
  },
  components: {
    CommentListItem,
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createComment: function () {
      const commentItem = {
        content: this.content,
        user: this.user,
        username: this.username,
        article: this.articleId,
      }
      if (commentItem.content) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/community/${this.articleId}/comment/`,
          data: commentItem,
          headers: this.getToken()
        })
          .then((res) => {
            this.content = null
            this.comment = res.data
            this.comments.push(this.comment)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
  },
  created: function(){
    const token = localStorage.getItem('jwt')
    // console.log(jwt_decode(token))
    this.user = jwt_decode(token).user_id
    axios({
      method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.user}/`,
        headers: this.getToken()
      })
        .then((res) => {
          // console.log(res)
          this.username = res.data.first_name
        })
        .catch((err) => {
          console.log(err)
        })
        
    axios({
          method: 'get',
          url: `http://127.0.0.1:8000/community/${this.articleId}/comment/`,
          headers: this.getToken()
        })
          .then((res) => {
            this.comments = res.data
          })
          .catch((err) => {
            console.log(err)
          })
  },
  watch: { comments:function () {
    axios({
          method: 'get',
          url: `http://127.0.0.1:8000/community/${this.articleId}/comment/`,
          headers: this.getToken()
    })
      .then((res) => {
        console.log(res)
        this.comments = this.res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }}
}
</script>

<style>

</style>