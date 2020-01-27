const md = require('markdown-it')();
const container = require('markdown-it-container');
const environment = require('dotenv').config();

if (environment.error) {
  console.error("You must provide proper Canvas credentials in the .env file");
  throw environment.error;
}

md.use(container, 'note', {

  validate: (params) => {
    console.log(`+${params.trim()}+`)
    return params.trim().match(/^note\s+(.*)$/);
  },

  render: (tokens, idx) => {
    let m = tokens[idx].info.trim().match(/^note\s+(.*)$/);

    if (tokens[idx].nesting === 1) {
      // opening tag
      return `<blockquote class="note"><strong> Note </strong>${md.utils.escapeHtml(m[1])}`
      //return '<details><summary>' + md.utils.escapeHtml(m[1]) + '</summary>\n';

    } else {
      // closing tag
      return '</blockquote>\n';
    }
  }
});

const result = md.render(`

::: note Testing this markdown :::

`);

console.log("result", JSON.stringify(result));
