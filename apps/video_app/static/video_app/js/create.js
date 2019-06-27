/* eslint-disable func-names */
/* eslint-disable prefer-arrow-callback */


function youtube_parser(url) {
  let regExp = /^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#\&\?]*).*/;
  let match = url.match(regExp);
  return (match && match[7].length == 11) ? match[7] : false;
}


$(document).ready(function () {
  console.log('loaded');
  $('#url').change(function () {
    let youtube_id = youtube_parser($('#url').val());

    $.ajax({
      url: 'https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=' + youtube_id + '&key=AIzaSyC_Rr6LKYWycQH-sYikgNswVOJj4k0t9aQ',
      method: 'GET',
    }).done(function (res) {
      if ($('#title').val() === '') {
        $('#title').val(res.items[0].snippet.title);
      }
      if ($('#description').val() === '') {
        $('#description').val(res.items[0].snippet.description);
      }
    });
  });
});
