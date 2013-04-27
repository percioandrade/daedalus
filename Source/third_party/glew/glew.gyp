{
  'targets': [
    {
      'target_name': 'glew',
      'type': 'static_library',
      'xcode_settings': {
        'OTHER_CFLAGS': [
          #'-Werror',
          '-O3',
          '-g'
        ],
      },
      'direct_dependent_settings': {
        'include_dirs': [
          'include/',
        ],
        'defines': [
          'GLEW_STATIC',
        ],
      },
      'include_dirs': [
        'include/',
      ],
      'sources': [
        'src/glew.c',
        'src/glewinfo.c',
        'src/visualinfo.c',
      ],
    }
  ],
}
