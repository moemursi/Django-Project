$( document ).ready(function () {
  const upload = $('.upload');
  const loading = $('.loading');
  const validExts = [".xlsx", ".xls"];
  $('.parse-file').click(function () {
    const file = $(".input-upload")[0].files[0]
    if (!file) {
      return;
    }
    const fileExt = file.name.substring(file.name.lastIndexOf('.'));
    var formData = new FormData();
    formData.append('file', $(".input-upload")[0].files[0]);
    if (validExts.indexOf(fileExt) < 0) {
      alert('Only .xlsx and .xls formats are valid');
    } else {
      upload.toggle('hidden');
      loading.toggle('hidden');
      $.ajax({
        type: "POST",
        url: this.dataset.url,
        data: formData,
        mimeType: "multipart/form-data",
        processData: false,
        headers: {'Authorization': `jwt ${this.dataset.token}`},
        success: (data) => {
          location.reload()
          alert('File was parsed successfully')
        },
        error: (data) => {
          upload.toggle('hidden')
          loading.toggle('hidden')
          alert(`Error: ${data.responseText}`);
        }
      });
    }
  });
});
