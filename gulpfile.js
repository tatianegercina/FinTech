const gulp = require("gulp");
const styleFmt = require("gulp-stylefmt");
const styleLint = require("gulp-stylelint");
const imagemin = require('gulp-imagemin');

const cssFiles = ["**/*.css", "!**/*.min.css",
  "!**/reset.css", "!**/normalize.css"];

gulp.task("stylefmt", () =>
  gulp.src(cssFiles)
    .pipe(styleFmt())
    .pipe(gulp.dest(""))
);

gulp.task("stylelint", () =>
  gulp
  .src(cssFiles)
  .pipe(styleLint({
    reporters: [
      {
        formatter: "string",
        console: true
      }
    ]
  }))
);

gulp.task("autofix", ["stylefmt"]);

gulp.task("lint", ["stylelint"]);

gulp.task('imagemin', () =>
  gulp.src('**/*.{gif,png,jpg}')
    .pipe(imagemin({verbose: true}))
    .pipe(gulp.dest('.'))
);
