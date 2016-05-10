{
  'targets': [
    {
      'target_name': 'uws',
      'sources': [
        'src/uWS.cpp',
        'src/addon.cpp'
      ],
      'conditions': [
        ['OS=="linux"', {
          'cflags_cc': [ '-fexceptions', '-std=c++11' ],
          'cflags_cc!': [ '-fno-exceptions' ]
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'CLANG_CXX_LANGUAGE_STANDARD':'c++11',
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'CLANG_CXX_LIBRARY': 'libc++'
          }
        }],
        ['OS=="win32"', {
          'cflags_cc': [],
          'cflags_cc!': []
        }]
       ]
    },
    {
      'target_name': 'action_after_build',
      'type': 'none',
      'dependencies': [ 'uws' ],
      'actions': [
        {
          'action_name': 'move_lib',
          'inputs': [
            '<@(PRODUCT_DIR)/uws.node'
          ],
          'outputs': [
            'uws'
          ],
          'action': ['cp', '<@(PRODUCT_DIR)/uws.node', 'uws_<!@(node -p process.platform)_<!@(node -p process.versions.modules).node']
        }
      ]
    }
  ]
}
