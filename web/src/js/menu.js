if (document.querySelector("section.section--menu")) {
  const itm = document.querySelector(
    "section.section--menu .section_content .desktopmenu"
  );
  const mob = document.querySelector(
    "section.section--menu .section_content .desktopmenu ol"
  );
  const cln = itm.cloneNode(true);
  document
    .querySelector("section.section--menu .cloneddesktopmenu")
    .appendChild(cln);
  const cln2 = mob.cloneNode(true);
  document
    .querySelector("section.section--menu .actualmobilemenu")
    .appendChild(cln2);

  var totalwidth;
  var bodytotalwidth;
  var cloneddesktopmenu = document.querySelector(
    "section.section--menu .section_content .cloneddesktopmenu .desktopmenu ol"
  );
  var desktopmenu = document.querySelector(
    "section.section--menu .section_content .actualdesktopmenu"
  );
  var mobilemenu = document.querySelector(
    "section.section--menu .actualmobilemenu"
  );
  var burgermenu = document.querySelector("section.section--menu .burgermenu");
  totalwidth = cloneddesktopmenu.clientWidth + 250;
  bodytotalwidth = document.querySelector("body").clientWidth;
  checkformobile();
  window.addEventListener("resize", () => {
    totalwidth = cloneddesktopmenu.clientWidth + 250;
    bodytotalwidth = document.querySelector("body").clientWidth;
    checkformobile();
  });

  function checkformobile() {
    if (totalwidth >= bodytotalwidth) {
      if (desktopmenu.classList.contains("makemobile")) {
      } else {
        desktopmenu.classList.add("opacitymakemobile");
        setTimeout(() => {
          desktopmenu.classList.remove("opacitymakemobile");
          desktopmenu.classList.add("makemobile");
          mobilemenu.classList.add("activatemobile");
          burgermenu.classList.add("activatemobile");
        }, 300);
      }
    } else {
      if (desktopmenu.classList.contains("makemobile")) {
        if (desktopmenu.classList.contains("makemobile")) {
          desktopmenu.classList.remove("makemobile");
          mobilemenu.classList.remove("activatemobile");
          burgermenu.classList.remove("activatemobile");
        } else {
        }
      }
    }
  }

  const burgermenubtn = document.querySelector(".section--menu .burgermenu");
  const actualmobile = document.querySelector(
    ".section--menu .actualmobilemenu"
  );
  if (!actualmobile.classList.contains("hidden")) {
    actualmobile.classList.add("hidden");
  }
  if (burgermenubtn.classList.contains("active")) {
    burgermenubtn.classList.remove("active");
  }
  burgermenubtn.addEventListener("click", () => {
    if (burgermenubtn.classList.contains("active")) {
      burgermenubtn.classList.toggle("active");
      actualmobile.classList.toggle("beforehidden");
      if (!actualmobile.classList.contains("beforehidden")) {
        actualmobile.classList.add("beforehidden");
      }
      setTimeout(() => {
        if (actualmobile.classList.contains("beforehidden")) {
          actualmobile.classList.remove("beforehidden");
        }
        actualmobile.classList.toggle("hidden");
      }, 500);
    } else {
      burgermenubtn.classList.toggle("active");
      actualmobile.classList.toggle("hidden");
    }
  });
}
