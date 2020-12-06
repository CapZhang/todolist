<template>
  <section class="todo-input">
    <div>
      <input
        type="text"
        placeholder="请输入代办事项"
        v-model="text"
        v-on:input="inputText"
        v-on:keyup.enter="addItem"
        class="todo-input-text"
      />
      <button v-on:click="addItem" class="todo-input-add-button">添加</button>
      <div>
        <datetime
          type="datetime"
          v-model="datetime"
          format="yyyy-MM-dd HH:mm:ss"
          hidden-name="123123"
          auto
        ></datetime>
        <button v-on:click="del_time">取消时间</button>
      </div>
      <span>展示：{{ chDate(datetime) }}</span>
    </div>
  </section>
</template>

<script>
// 时间组件=> https://github.com/mariomka/vue-datetime
import { Datetime } from "vue-datetime";
import "vue-datetime/dist/vue-datetime.css";
import dayjs from "dayjs";

export default {
  components: {
    datetime: Datetime,
  },
  data() {
    return {
      text: "",
      datetime: null,
      dayjs: dayjs,
      chDate(time) {
        return this.dayjs(time).format("YYYY-MM-DD HH:mm:ss");
      },
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
        if (this.datetime) {
          this.inputArry[0].deadline = this.chDate(this.datetime);
          console.log(this.inputArry[0].deadline);
        }
        this.$store.dispatch("addItem", this.inputArry);
        this.inputArry = "";
        this.text = "";
        this.datetime = "";
        console.log(this.$store.items);
      }
    },
    del_time() {
      console.log("点击前=>", this.datetime);
      this.datetime = "";
      if (this.inputArry) {
        this.inputArry[0].deadline = "";
      }
      console.log("点击后=>", this.datetime);
    },
  },
};
</script>