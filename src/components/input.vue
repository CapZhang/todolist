<template>
  <section class="todo-input">
    <input
      type="text"
      placeholder="请输入代办事项"
      v-model="text"
      v-on:input="inputText"
      v-on:keyup.enter="addItem"
    />
    <button v-on:click="addItem">添加</button>
    <br>
    <datetime
      type="datetime"
      v-model="datetime"
      format="yyyy-MM-dd HH:mm:ss"
      auto
    ></datetime>
    <span>展示：{{ chDate(datetime) }}</span>
  </section>
</template>

<script>
import { Datetime } from "vue-datetime";
import "vue-datetime/dist/vue-datetime.css";
import dayjs from "dayjs"

export default {
  components: {
    datetime: Datetime,
  },
  data() {
    return {
      text: "",
      datetime: null,
      dayjs: dayjs,
      chDate(time){
        return this.dayjs(time).format('YYYY-MM-DD HH:mm:ss');
      }
    };
  },
  methods: {
    inputText(e) {
      if (e.target.value != "") {
        this.inputArry = [{ name: e.target.value }];
      }
    },
    addItem() {
      if (this.inputArry != "") {
        if(this.datetime){
          this.inputArry[0].deadline = this.chDate(this.datetime)
          console.log(this.inputArry[0].deadline);
        }
        this.$store.dispatch("addItem", this.inputArry);
        this.inputArry = "";
        this.text = "";
        console.log(this.$store.items);
      }
    },
  },
};
</script>