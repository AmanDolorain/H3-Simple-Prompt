import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
let extension;
vm.runInNewContext(fs.readFileSync(new URL('../web/fields.js',import.meta.url),'utf8').replace(/^import .*;\n/,''),{app:{registerExtension:e=>extension=e},Array});
class FakeNode {constructor(){this.widgets=[{name:'text',value:''}];}onConfigure(info){this.widgets[0].value=info.widgets_values[0];}}
extension.beforeRegisterNodeDef(FakeNode,{name:'AmanSimplePrompt'});
const old=new FakeNode();old.onConfigure({widgets_values:['  Old prompt\nਸਤ ਸ੍ਰੀ ਅਕਾਲ।  ']});
assert.equal(old.widgets[0].value,'  Old prompt\nਸਤ ਸ੍ਰੀ ਅਕਾਲ।  ');
const structured=new FakeNode();structured.onConfigure({widgets_values:['trigger','character','summary','retention','scene','light','action','camera','dialogue','sfx','score']});
assert.equal(structured.widgets[0].value,'trigger\n\nsubject_definitions:\ncharacter\n\nsummary:\nsummary\n\nretention_analysis:\nretention\n\ndetailed_description:\nscene\n\nlight\n\naction\n\ncamera\n\ndialogue\n\noverall_soundscape:\nsfx\n\nnon_diegetic_music:\nscore');
const empty=new FakeNode();empty.onConfigure({widgets_values:Array(11).fill('')});assert.equal(empty.widgets[0].value,'');
console.log('PASS: old single prompt unchanged; all structured fields merged without losing content; empty migration');
