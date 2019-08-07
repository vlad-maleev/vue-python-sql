<template>
  <div id="app">
    <transition appear name="slide-fade">
      <div class="form">
        <b-form-file
          v-model="file"
          :state="Boolean(file)"
          placeholder="Choose a file..."
          drop-placeholder="Drop file here..."
        ></b-form-file>
        <div class="mt-3">Selected file: {{ file ? file.name : '' }}</div>
        <b-button pill variant="success" @click="submitFile">SUBMIT</b-button>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      file: null,
      }
  },
  methods: {
    submitFile() {
      let formData = new FormData();

      formData.append("file", this.file, this.file.name);

      axios
        .post("http://localhost:5000/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(res => {
          console.log("SUCCESS!!");
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
};
</script>

<style>
body {
  height: 90vh;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
}

.form {
  width: 300px;
}

.btn {
  margin-top: 50px;
}

/* animations */

.slide-fade-enter-active {
  transition: all 1s ease;
}

.slide-fade-enter {
  transform: translateY(-100px);
  opacity: 0;
}
</style>
