<template>
  <div id="app">
    <!-- <form></form>
    <label>
      Upload your file
      <br />
      <br />
      <input type="file" id="file" ref="file" name="inputFile" @change="handleFileUpload" />
    </label>
    <hr />
    <hr />
    <button @click="submitFile">Submit</button>

    <hr />
    <hr />-->

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

    <!-- <p v-for="book in books" :key="book.title">
      Author: {{ book.author }}; 
      <br>
      Title: "{{ book.title }}"</p>
    <hr />
    <hr />
    <hr />
    <button @click="addBook">Add sample book</button>-->
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      file: null,
      msg: "",
      books: [],
      payload: {
        title: "Some title",
        author: "John Smith",
        read: true
      }
    };
  },
  methods: {
    // handleFileUpload(event) {
    //   this.file = event.target.files[0];
    // },

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

    //connection checking
    //
    // getMessage() {
    //   //getting test message
    //   axios
    //     .get("http://localhost:5000/ping")
    //     .then(res => {
    //       this.msg = res.data;
    //     })
    //     .catch(err => {
    //       console.log(err);
    //     });
    // },

    // getBooks() {
    //   axios
    //     .get("http://localhost:5000/books")
    //     .then(res => {
    //       this.books = res.data.books;
    //       console.log(this.books);
    //     })
    //     .catch(err => {
    //       console.log(err);
    //     });
    // },

    // addBook() {
    //   const path = "http://localhost:5000/books";
    //   axios
    //     .post(path, this.payload)
    //     .then(() => {
    //       this.getBooks();
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // }
  },
  created() {
    // this.getMessage();
    // this.getBooks();
  }
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
