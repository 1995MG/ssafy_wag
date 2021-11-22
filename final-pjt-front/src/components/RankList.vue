<template>
  <div>
    <div class="d-flex justify-content-between">
      <h5 class="fw-bold">평점</h5>
      <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#Modal">평점등록</button>
      <!-- 평점등록모달 -->
      <div class="modal fade" id="Modal" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title fw-bold" id="ModalLabel">평점등록</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div class="input-group mb-3">
                <label class="input-group-text" for="inputGroupSelect01">평점</label>
                <select v-model="score" class="form-control" id="inputGroupSelect01">
                  <option value="10">10</option>
                  <option value="9">9</option>
                  <option value="8">8</option>
                  <option value="7">7</option>
                  <option value="6">6</option>
                  <option value="5">5</option>
                  <option value="4">4</option>
                  <option value="3">3</option>
                  <option value="2">2</option>
                  <option value="1">1</option>
                </select>
              </div>
              <textarea v-model="content" class="form-control" placeholder="내용을 입력하세요." rows="20"></textarea>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">취소</button>
              <button @click="createRank" type="button" class="btn btn-success" data-bs-dismiss="modal">평점등록</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <rank-list-item class="container"
      v-for="rank in ranks"
      :key="rank.id"
      :ranks="ranks"
      :rank="rank"
    >
    </rank-list-item>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
import jwt_decode from 'jwt-decode'
import RankListItem from '@/components/RankListItem.vue'
export default {
  name: 'RankList',
  data: function ()   {
    return {
      ranks: [],
      rank: null,
      score: null,
      content: null,
      user: null,
      username: null,
    }
  },
  props: {
    movieId: [String, Number],
  },
  components: {
    RankListItem
  },
  methods: {
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createRank: function () {
      const rankItem = {
        score: this.score,
        content: this.content,
        user: this.user,
        username: this.username,
        movie: this.movieId,
      }
      if (rankItem.content) {
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/movies/${this.movieId}/rank/`,
          data: rankItem,
          headers: this.getToken()
        })
          .then((res) => {
            this.score = null
            this.content = null
            this.rank = res.data
            this.ranks.push(this.rank)
            // console.log(res.data)
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
          url: `http://127.0.0.1:8000/movies/${this.movieId}/rank/`,
          headers: this.getToken()
        })
          .then((res) => {
            this.ranks = res.data
            // this.ranks = _.orderBy(res.data, 'likes_users', 'desc')
          })
          .catch((err) => {
            console.log(err)
          })
  },
}
</script>

<style>

</style>