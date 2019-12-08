const rand = document.getElementById('form')
const slidesInner = slides.querySelector('.slides-inner')
const text = document.getElementById('textSlide')
const sub_button = document.getElementById('random_sentence')
const num = rand.querySelector("input[type='number']")


sub_button.addEventListener('click', function(e){
  let q = 10
  if (num.value) {
    q = num.value
  }

  // /data?q=${q}&book=a
  fetch(`/data?q=${q}`).then(function(res) {
    return res.json()
  }).then(function(json) {
    const h3 = document.querySelector('h3')
    mySlides.nextSlide()
    // Use the JSON data to populate these elements
    h3.innerHTML = json.sentence 
    text.innerHTML = json.sentence
  }).catch(function(err) {
    console.error(err.message)
  })
})



const slideshow = document.querySelector('.ms-slide-show')
const mySlides = makeSlideshow(slideshow)






