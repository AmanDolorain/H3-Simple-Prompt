import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('aman_prompt', ROOT / '__init__.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class PromptTests(unittest.TestCase):
    def test_comfy_registration_and_blank_multiline_widget(self):
        cls = module.NODE_CLASS_MAPPINGS['AmanSimplePrompt']
        self.assertEqual(module.NODE_DISPLAY_NAME_MAPPINGS['AmanSimplePrompt'], 'H3 Simple Prompt')
        self.assertEqual(cls.RETURN_TYPES, ('STRING',))
        self.assertEqual(cls.RETURN_NAMES, ('prompt',))
        fields = cls.INPUT_TYPES()
        self.assertEqual(list(fields['required']), ['text'])
        kind, options = fields['required']['text']
        self.assertEqual(kind, 'STRING')
        self.assertEqual(options['default'], '')
        self.assertTrue(options['multiline'])
        self.assertFalse(options['dynamicPrompts'])
        self.assertTrue((ROOT / module.WEB_DIRECTORY / 'author.js').is_file())

    def test_literal_h3_and_multilingual_text(self):
        for text in ('', '  leading and trailing  ', 'Line 1\n\nLine 2\r\n',
                     '<Picture 1> <Picture 2> <Picture 3> <Video 1> <Audio 1>',
                     'आदमी धीरे चलता है।\nਉਹ ਗੀਤ ਗਾਉਂਦਾ ਹੈ। ♪',
                     '{red|blue} @tag *literal* #line "quoted"', 'a'*100000):
            with self.subTest(text=text[:60]):
                self.assertEqual(module.AmanSimplePrompt().get_prompt(text), (text,))

    def test_starter_workflow_matches_schema(self):
        data=json.loads((ROOT / 'Simple_Prompt_Starter.json').read_text())
        node=data['nodes'][0]
        self.assertIn(node['type'], module.NODE_CLASS_MAPPINGS)
        self.assertEqual(node['widgets_values'], [''])
        self.assertEqual(node['outputs'][0]['type'], 'STRING')
        self.assertEqual(data['links'], [])

if __name__ == '__main__':
    unittest.main()
