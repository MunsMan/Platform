const gulp = require("gulp");
const sass = require("gulp-sass");
const browserSync = require("browser-sync").create();

// Compiler
function style() {
  return gulp
    .src("./web/src/scss/main.scss")
    .pipe(sass())
    .pipe(gulp.dest("./web/src/css"))
    .pipe(browserSync.stream());
}
// Watch
function watch() {
  browserSync.init({
    server: {
      baseDir: "./web"
    }
  });
  gulp.watch("./web/src/scss/**/*.scss", style);
  gulp.watch("./web/src/scss/**/*.sass", style);
  gulp.watch("./web/src/**/*.html").on("change", browserSync.reload);
  gulp.watch("./web/src/**/*.php").on("change", browserSync.reload);
  gulp.watch("./web/src/**/*.js").on("change", browserSync.reload);
}

exports.style = style;
exports.watch = watch;
