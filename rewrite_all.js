const fs = require('fs');

// 1. Split content.yml into separate files
if (fs.existsSync('_data/content.yml')) {
    const jsyaml = require('./admin/js-yaml.min.js'); // wait, do we have jsyaml? Let's check if we can run it.
    console.log("No js-yaml available in node. using simple string parsing");
}
