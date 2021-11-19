<template>
  <div class="container">
    <div class="my-5 input-group-lg">
      <div class="d-flex justify-content-between">
        <h1 class="fw-bold">커뮤니티 글 수정</h1>
        <button @click="updateArticle" class="btn btn-success btn-lg">수정</button>
      </div>
      <hr>
      <input :value="title" @input="title=$event.target.value" class="form-control" type="text">
      <br>
      <textarea :value="content" @input="content=$event.target.value" class="form-control" rows="30"></textarea>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'ArticleUpdateForm',
  data: function () {
    return {
      title:this.$route.query.article.title,
      content: this.$route.query.article.content,
      user: null,
      username: null,
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
    updateArticle: function () {
      const articleItem = {
        title: this.title,
        content: this.content,
        user: this.user,
        username: this.username
      }
      if (articleItem.title) {
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/community/${this.$route.query.article.id}/`,
          data: articleItem,
          headers: this.setToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name : 'Community' })
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },
  },
  created: function () {
    console.log(this.$route.query)
    // this.title = this.$route.query.article.title
    // this.content = this.$route.query.article.content
    
    const token = localStorage.getItem('jwt')
    // console.log(jwt_decode(token))
    this.user = jwt_decode(token).user_id

    axios({
      method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.user}/`,
        headers: this.setToken()
      })
        .then((res) => {
          // console.log(res)
          this.username = res.data.first_name
        })
        .catch((err) => {
          console.log(err)
        })

    
  }
}
</script>

<style>

</style>