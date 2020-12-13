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
        <ul class="todo-info-border">
          <li style="float: right">
            <input
              type="radio"
              name="level"
              id="IN"
              value="IN"
              v-model="level"
            />
            <label for="IN" class="level-info">重要紧急</label>
            <input
              type="radio"
              name="level"
              id="UU"
              value="UU"
              v-model="level"
            />
            <label for="UU" class="level-info">不重要紧急</label>
            <br />
            <input
              type="radio"
              name="level"
              id="IU"
              value="IU"
              v-model="level"
            />
            <label for="IU" class="level-info">重要不紧急</label>
            <input
              type="radio"
              name="level"
              id="UN"
              value="UN"
              v-model="level"
            />
            <label for="UN" class="level-info">不重要不紧急</label>
          </li>
          <li>
            <button
              v-on:click="del_time('deadline')"
              class="clear-info clear-float"
            >
              ×
            </button>
            <datetime
              type="datetime"
              v-model="input_deadline"
              format="yyyy-MM-dd HH:mm:ss"
              hidden-name="123123"
              auto
            ></datetime>
            <span class="todo-info">截止时间： </span>
          </li>
          <li>
            <button
              v-on:click="del_time('reminder')"
              class="clear-info clear-float"
            >
              ×
            </button>
            <datetime
              type="datetime"
              v-model="input_reminder"
              format="yyyy-MM-dd HH:mm:ss"
              hidden-name="123123"
              auto
            ></datetime>
            <span class="todo-info">提醒时间： </span>
          </li>
        </ul>
      </div>
      <br />
      <!-- <span>展示：{{ chDate(datetime) }}</span> -->
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
      inputArry: "",
      level: "IN",
      text: "",
      input_deadline: null,
      input_reminder: null,
      dayjs: dayjs,
      chDate(time) {
        return this.dayjs(time).format("YYYY-MM-DD HH:mm:ss");
      },
    };
  },
  methods: {
    inputText(e) {
      if (e.target.value != "") {
        console.log("add之前的items=>", this.$store.state.items);
        this.inputArry = [{ name: e.target.value }];
      }
    },
    addItem() {
      if (this.inputArry != "") {
        console.log("添加待办=>", this.inputArry);
        if (this.input_deadline) {
          this.inputArry[0].deadline = this.chDate(this.input_deadline);
          console.log(this.inputArry[0].deadline);
        }
        if (this.input_reminder != "") {
          this.inputArry[0].reminder_time = this.chDate(this.input_reminder);
          console.log(this.inputArry[0].reminder_time);
        }
        if (this.level) {
          this.inputArry[0].level = this.level;
          console.log(this.inputArry[0].level);
        }
        for (let i = 0; i < this.$store.state.items.length; i++) {
          console.log("name=>", this.$store.state.items[i].name);
          if (this.$store.state.items[i].name == this.inputArry[0].name) {
            this.inputArry = "";
            this.text = "";
            this.input_deadline = "";
            this.input_reminder = "";
            return alert("已存在");
          }
        }
        this.$https
          .post("/todo/post", this.inputArry)
          .then((res) => {
            if (res.data.code == 0) {
              // let updateStatus = {}
              // this.$store.dispatch("updateStatus", updateStatus);
              console.log("input新增待办=>", res);
            } else {
              alert("网络错误:" + res.data.message);
            }
          })
          .catch((err) => {
            return err;
          });
        this.$store.dispatch("addItem", this.inputArry);
        this.inputArry = "";
        this.text = "";
        this.input_deadline = "";
        this.input_reminder = "";
        console.log(this.$store.items);
      }
    },
    del_time(type) {
      if (type == "deadline") {
        console.log("点击前=>", this.input_deadline);
        this.input_deadline = "";
        if (this.inputArry) {
          this.inputArry[0].deadline = "";
        }
        console.log("点击后=>", this.datetime);
      } else if (type == "reminder") {
        console.log("点击前=>", this.input_reminder);
        this.input_reminder = "";
        if (this.inputArry) {
          this.inputArry[0].reminder_time = "";
        }
        console.log("点击后=>", this.datetime);
      } else {
        this.inputArry = "";
      }
    },
  },
};
</script>