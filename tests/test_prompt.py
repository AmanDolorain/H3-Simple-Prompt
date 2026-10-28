import importlib.util
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('aman_prompt',ROOT/'__init__.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class PromptTests(unittest.TestCase):
    def test_single_blank_multiline_schema(self):
        cls=module.NODE_CLASS_MAPPINGS['AmanSimplePrompt']
        fields=cls.INPUT_TYPES()['required']
        self.assertEqual(list(fields),['text'])
        self.assertEqual(cls.RETURN_TYPES,('STRING',))
        self.assertEqual(cls.RETURN_NAMES,('prompt',))
        kind,options=fields['text']
        self.assertEqual(kind,'STRING');self.assertEqual(options['default'],'')
        self.assertTrue(options['multiline']);self.assertFalse(options['dynamicPrompts'])
        self.assertEqual(module.NODE_DISPLAY_NAME_MAPPINGS['AmanSimplePrompt'],'H3 Simple Prompt')

    def test_preserves_literal_prompts_and_complete_structure(self):
        texts=['','  whitespace  ','Line 1\n\nLine 2\r\n',
               '<Picture 1> <Video 1> <Audio 1>','ਆਦਮੀ ਗਾਉਂਦਾ ਹੈ।\nआदमी चलता है।',
               '{red|blue} @tag *x* #line','a'*100000,
               'subject_definitions:\nA man.\n\ndetailed_description:\n[Shot 1] He waves.\n[Shot 2] At 00:03.000, cut.\n\noverall_soundscape:\nWind.']
        for text in texts:
            self.assertEqual(module.AmanSimplePrompt().get_prompt(text),(text,))

    def test_starter_matches_current_schema(self):
        node=json.loads((ROOT/'Simple_Prompt_Starter.json').read_text())['nodes'][0]
        self.assertEqual(node['widgets_values'],[''])
        self.assertEqual(node['type'],'AmanSimplePrompt')
        self.assertEqual(node['outputs'][0]['type'],'STRING')

if __name__=='__main__':unittest.main()
