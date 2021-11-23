<template>
  <div class="signin container text-white">
    <h1 class="fw-bold">로그인</h1>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="username">아이디</label>
      <br>
      <input v-model="credentials.username" class="form-control" type="text" id="username">
    </div>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="password">비밀번호</label>
      <br>
      <input @keyup.enter="signin" v-model="credentials.password" class="form-control" type="password" id="password">
    </div>
    <button @click="signin" class="btn btn-success btn-lg my-3">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signin',
  data: function () {
    return {
      credentials: {
      }
    }
  },
  methods: {
    signin: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then((res) => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('signin')
          this.$router.push({ name: 'Profile' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
}
</script>

<style>

</style>