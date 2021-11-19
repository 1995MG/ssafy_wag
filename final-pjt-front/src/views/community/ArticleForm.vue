<template>
  <div class="articleform container">
    <div class="my-5 input-group-lg">
      <div class="d-flex justify-content-between">
        <h1 class="fw-bold">커뮤니티 글쓰기</h1>
        <button @click="createArticle" class="btn btn-success btn-lg">등록</button>
      </div>
      <hr>
      <input v-model="title" class="form-control" type="text" placeholder="제목을 입력해 주세요.">
      <br>
      <textarea v-model="content" class="form-control" placeholder="내용을 입력하세요." rows="30"></textarea>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

export default {
  name: 'ArticleForm',
  data: function () {
    return {
      title: null,
      content: null,
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
    createArticle: function () {
      const articleItem = {
        title: this.title,
        content: this.content,
        user: this.user,
        username: this.username
      }
      if (articleItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/community/',
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