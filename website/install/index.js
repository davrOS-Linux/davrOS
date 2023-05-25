function clipboard() {
      var code_box = document.getElementById("code");
      code_box[0].select();
      code_box.setSelectionRange(0, 99999);
      navigator.clipboard.writeText(code_box.value);
      alert("Copied the text: " + copyText.value);
      document.getElementById("clipboard_button").innerHTML = "☑";
} 
