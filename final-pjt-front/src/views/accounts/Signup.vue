<template>
  <div class="signup container">
    <h1 class="fw-bold">회원가입</h1>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="username">아이디</label>
      <br>
      <input v-model="credentials.username" class="form-control" type="text" id="username">
    </div>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="password">비밀번호</label>
      <br>
      <input v-model="credentials.password" class="form-control" type="password" id="password">
    </div>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="passwordConfirmation">비밀번호 확인</label>
      <br>
      <input v-model="credentials.passwordConfirmation" class="form-control" type="password" id="passwordConfirmation">
    </div>
    <div class="my-3 input-group-lg">
      <label class="fw-bold mb-1" for="first_name">이름</label>
      <br>
      <input v-model="credentials.first_name" class="form-control" type="text" id="first_name">
    </div>
    <button @click="signup" class="btn btn-success btn-lg my-3">가입하기</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Signup',
  data: function() {
    return {
      credentials: {
      }
    }
  },
  methods: {
    signup: function () {
      console.log(this.credentials)
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'Signin' })
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