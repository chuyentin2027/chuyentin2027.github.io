import os
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_markdown_table(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    header_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('| Tên Tỉnh |'):
            header_idx = i
            break

    if header_idx == -1:
        print("Header not found in markdown!")
        return []

    data = []
    for i in range(header_idx + 2, len(lines)):
        line = lines[i].strip()
        if not line.startswith('|') or not line.endswith('|'):
            break
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 5:
            prov = parts[0]
            school = parts[1]
            year = parts[2]
            link_cell = parts[3]
            download_cell = parts[4]

            # Extract title and original URL
            title_m = re.search(r'\[Xem đề thi:\s*([^\]]+)\]\(([^)]+)\)', link_cell)
            if title_m:
                title = title_m.group(1).strip()
                orig_url = title_m.group(2).strip()
            else:
                title = f"Đề thi {prov} {year}"
                orig_url = "#"

            # Extract PDF link
            pdf_m = re.search(r'\[([^\]]+\.pdf)\]\(([^)]+)\)', download_cell)
            if pdf_m:
                pdf_name = pdf_m.group(1).strip()
                pdf_url = f"dethi/{pdf_name}"
                has_pdf = True
            else:
                pdf_name = None
                pdf_url = None
                has_pdf = False

            data.append({
                'id': len(data) + 1,
                'province': prov,
                'school': school,
                'year': year,
                'title': title,
                'original_url': orig_url,
                'has_pdf': has_pdf,
                'pdf_name': pdf_name,
                'pdf_url': pdf_url
            })

    return data

def build_html_page(data, out_path):
    json_data = json.dumps(data, ensure_ascii=False)
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hệ Thống Đề Thi & Lời Giải Chuyên Tin Lớp 10 Toàn Quốc</title>
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Supabase JS Client -->
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    
    <!-- Highlight.js for Syntax Highlighting -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/cpp.min.js"></script>

    <!-- Supabase Config -->
    <script src="config.js"></script>

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['"Plus Jakarta Sans"', 'system-ui', '-apple-system', 'sans-serif'],
                        mono: ['"Fira Code"', 'Consolas', 'Monaco', 'monospace'],
                    }},
                    fontSize: {{
                        '2xs': '0.6875rem', /* 11px */
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{
            background-color: #0b1120;
            color: #f1f5f9;
        }}
        .custom-scrollbar::-webkit-scrollbar {{
            width: 5px;
            height: 5px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}
        pre code.hljs {{
            border-radius: 0.5rem;
            padding: 0.75rem 1rem;
            font-size: 0.75rem;
            line-height: 1.5;
        }}
    </style>
</head>
<body class="min-h-screen font-sans antialiased text-slate-100 bg-[#0b1120] text-xs leading-relaxed flex flex-col justify-between">

    <div>
        <!-- Navbar / Header -->
        <header class="border-b border-slate-800/80 bg-slate-900/80 backdrop-blur-md sticky top-0 z-30 shadow-md">
            <div class="w-full max-w-[1750px] mx-auto px-2 sm:px-4 h-13 py-2.5 flex items-center justify-between">
                <div class="flex items-center gap-2.5">
                    <div class="w-7 h-7 rounded-lg bg-gradient-to-tr from-indigo-600 to-cyan-500 flex items-center justify-center shadow-md shadow-indigo-500/20 ring-1 ring-indigo-400/30">
                        <i class="fa-solid fa-code text-white text-xs"></i>
                    </div>
                    <div>
                        <h1 class="font-bold text-xs sm:text-sm tracking-tight text-white flex items-center gap-2">
                            Đề Thi & Lời Giải Chuyên Tin Lớp 10
                            <span class="hidden md:inline-block px-2 py-0.5 text-[10px] font-semibold bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 rounded-full">2019 - 2026</span>
                        </h1>
                        <p class="text-2xs text-slate-400 font-normal hidden sm:block">Tra cứu đề thi, xem PDF trực tuyến & đóng góp lời giải Python</p>
                    </div>
                </div>
                
                <div class="flex items-center gap-2">
                    <!-- Database Status Button -->
                    <button onclick="openConfigModal()" id="db-status-btn" class="inline-flex items-center gap-1.5 px-2.5 py-1 text-2xs font-semibold rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition" title="Cấu hình Cloud Database Supabase">
                        <span id="db-status-dot" class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        <span id="db-status-text" class="hidden sm:inline">Database: Supabase Cloud</span>
                        <i class="fa-solid fa-gear text-[10px] text-slate-400"></i>
                    </button>
                </div>
            </div>
        </header>

        <!-- Main Content (Ultra Wide) -->
        <main class="w-full max-w-[1750px] mx-auto px-2 sm:px-3.5 py-2.5 space-y-2.5">
            
            <!-- Quick Stats & Filter Controls -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-2">
                
                <!-- Quick Stats (3 cards compact) -->
                <div class="lg:col-span-4 grid grid-cols-3 gap-1.5">
                    <div class="bg-slate-900/80 border border-slate-800 rounded-lg p-2 flex flex-col justify-between shadow-sm">
                        <span class="text-2xs font-semibold text-slate-400 uppercase tracking-wider truncate">Tổng đề thi</span>
                        <div class="mt-0.5 flex items-baseline gap-1">
                            <span id="stat-total" class="text-sm sm:text-base font-bold text-white">0</span>
                            <span class="text-[10px] text-slate-500">đề</span>
                        </div>
                    </div>

                    <div class="bg-slate-900/80 border border-slate-800 rounded-lg p-2 flex flex-col justify-between shadow-sm">
                        <span class="text-2xs font-semibold text-slate-400 uppercase tracking-wider truncate">Đã tải PDF</span>
                        <div class="mt-0.5 flex items-baseline gap-1.5">
                            <span id="stat-pdf" class="text-sm sm:text-base font-bold text-emerald-400">0</span>
                            <span id="stat-pdf-percent" class="text-[10px] font-semibold px-1 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">0%</span>
                        </div>
                    </div>

                    <div class="bg-slate-900/80 border border-slate-800 rounded-lg p-2 flex flex-col justify-between shadow-sm">
                        <span class="text-2xs font-semibold text-slate-400 uppercase tracking-wider truncate">Bài giải Python</span>
                        <div class="mt-0.5 flex items-baseline gap-1">
                            <span id="stat-solutions" class="text-sm sm:text-base font-bold text-cyan-400">0</span>
                            <span class="text-[10px] text-slate-500">bài nộp</span>
                        </div>
                    </div>
                </div>

                <!-- Filter Controls -->
                <div class="lg:col-span-8 bg-slate-900/80 border border-slate-800 rounded-lg p-2 shadow-sm flex flex-col justify-center">
                    <div class="grid grid-cols-1 sm:grid-cols-12 gap-1.5">
                        
                        <!-- Search Input -->
                        <div class="sm:col-span-6 relative">
                            <i class="fa-solid fa-magnifying-glass absolute left-2.5 top-1/2 -translate-y-1/2 text-slate-500 text-xs"></i>
                            <input type="text" id="search-input" placeholder="Tìm kiếm tỉnh thành, trường, năm học hoặc tên đề thi..." 
                                class="w-full pl-7 pr-7 py-1.5 rounded bg-slate-950 border border-slate-700/70 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 transition">
                            <button id="clear-search" class="hidden absolute right-2 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white text-xs">
                                <i class="fa-solid fa-xmark"></i>
                            </button>
                        </div>

                        <!-- Province Filter -->
                        <div class="sm:col-span-3">
                            <select id="filter-province" class="w-full px-2 py-1.5 rounded bg-slate-950 border border-slate-700/70 text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500 transition">
                                <option value="">Tất cả tỉnh thành</option>
                            </select>
                        </div>

                        <!-- Year Filter -->
                        <div class="sm:col-span-2">
                            <select id="filter-year" class="w-full px-2 py-1.5 rounded bg-slate-950 border border-slate-700/70 text-xs text-slate-200 focus:outline-none focus:ring-1 focus:ring-indigo-500 transition">
                                <option value="">Tất cả năm</option>
                            </select>
                        </div>

                        <!-- Reset Button -->
                        <div class="sm:col-span-1 flex">
                            <button id="btn-reset-filters" title="Đặt lại bộ lọc" class="w-full py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 transition flex items-center justify-center gap-1 text-xs">
                                <i class="fa-solid fa-rotate-right text-2xs"></i>
                            </button>
                        </div>
                    </div>

                    <!-- Filter Status Bar -->
                    <div class="flex items-center justify-between pt-1 mt-1 border-t border-slate-800/80 text-[11px] text-slate-400">
                        <div class="flex items-center gap-1.5">
                            <span>Hiển thị:</span>
                            <span id="filtered-count" class="font-bold text-indigo-400">0</span>
                            <span id="total-count-label">/ 0 đề</span>
                        </div>
                        <div class="flex items-center gap-1.5">
                            <span>Sắp xếp:</span>
                            <span id="current-sort-label" class="text-slate-300 font-medium">Năm Học (Mới nhất)</span>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Full-Width Table Container (Maximized space) -->
            <div class="bg-slate-900/90 border border-slate-800 rounded-lg shadow-lg overflow-hidden">
                <div class="overflow-x-auto custom-scrollbar">
                    <table class="w-full text-left border-collapse text-xs">
                        <thead>
                            <tr class="bg-slate-950/90 border-b border-slate-800 text-slate-300 select-none">
                                <th scope="col" class="py-2 px-2 text-center w-10 cursor-pointer hover:text-indigo-400 transition" onclick="handleSort('id')">
                                    # <span class="sort-icon ml-0.5 text-2xs" data-col="id"></span>
                                </th>
                                <th scope="col" class="py-2 px-2.5 font-semibold whitespace-nowrap cursor-pointer hover:text-indigo-400 transition w-36" onclick="handleSort('province')">
                                    Tên Tỉnh <span class="sort-icon ml-0.5 text-2xs" data-col="province"></span>
                                </th>
                                <th scope="col" class="py-2 px-2.5 font-semibold cursor-pointer hover:text-indigo-400 transition min-w-[190px]" onclick="handleSort('school')">
                                    Tên Trường <span class="sort-icon ml-0.5 text-2xs" data-col="school"></span>
                                </th>
                                <th scope="col" class="py-2 px-2 font-semibold text-center whitespace-nowrap w-24 cursor-pointer hover:text-indigo-400 transition" onclick="handleSort('year')">
                                    Năm Học <span class="sort-icon ml-0.5 text-2xs" data-col="year">▼</span>
                                </th>
                                <th scope="col" class="py-2 px-2.5 font-semibold min-w-[240px]">
                                    Link Đề Thi Gốc
                                </th>
                                <th scope="col" class="py-2 px-2.5 font-semibold text-center whitespace-nowrap w-56 cursor-pointer hover:text-indigo-400 transition" onclick="handleSort('has_pdf')">
                                    Xem PDF & Lời Giải <span class="sort-icon ml-0.5 text-2xs" data-col="has_pdf"></span>
                                </th>
                            </tr>
                        </thead>
                        <tbody id="exam-table-body" class="divide-y divide-slate-800/50">
                            <!-- Dynamic rows rendered by JS -->
                        </tbody>
                    </table>
                </div>

                <!-- Empty State -->
                <div id="empty-state" class="hidden py-10 text-center">
                    <div class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center mx-auto text-slate-500 mb-2 text-base">
                        <i class="fa-solid fa-folder-open"></i>
                    </div>
                    <h3 class="text-xs font-semibold text-slate-300">Không tìm thấy đề thi phù hợp</h3>
                    <p class="text-2xs text-slate-500 mt-0.5 max-w-xs mx-auto">Vui lòng thử điều chỉnh lại từ khóa tìm kiếm hoặc đặt lại bộ lọc.</p>
                    <button onclick="resetFilters()" class="mt-2.5 px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white text-2xs font-semibold transition">
                        Xóa tất cả bộ lọc
                    </button>
                </div>

                <!-- Pagination Footer -->
                <div class="px-3 py-2 border-t border-slate-800 bg-slate-950/50 flex flex-col sm:flex-row items-center justify-between gap-2 text-2xs text-slate-400">
                    <div class="flex items-center gap-1.5">
                        <span>Dòng mỗi trang:</span>
                        <select id="page-size" class="px-1.5 py-0.5 rounded bg-slate-900 border border-slate-700 text-slate-200 text-2xs focus:outline-none">
                            <option value="25">25</option>
                            <option value="50" selected>50</option>
                            <option value="100">100</option>
                            <option value="9999">Tất cả</option>
                        </select>
                    </div>

                    <div class="flex items-center gap-1" id="pagination-controls">
                        <!-- Dynamic pagination buttons -->
                    </div>
                </div>
            </div>

        </main>
    </div>

    <!-- Maximum Workspace PDF & Solutions Modal / Popup -->
    <div id="pdf-modal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-0.5 sm:p-1 bg-slate-950/92 backdrop-blur-sm transition-opacity">
        <div id="pdf-modal-card" class="bg-slate-900 border border-slate-700/80 rounded-md w-full h-full max-w-[99.5vw] max-h-[99vh] flex flex-col shadow-2xl overflow-hidden">
            
            <!-- Compact Modal Header with Tabs & Controls -->
            <div class="px-2.5 py-1.5 border-b border-slate-800 flex items-center justify-between bg-slate-950 shrink-0">
                
                <!-- Left: Title & Info -->
                <div class="flex items-center gap-2 overflow-hidden mr-2">
                    <div class="w-6 h-6 rounded bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 flex items-center justify-center shrink-0">
                        <i class="fa-solid fa-graduation-cap text-xs"></i>
                    </div>
                    <div class="overflow-hidden">
                        <h3 id="pdf-modal-title" class="font-bold text-xs text-white truncate max-w-xs sm:max-w-sm md:max-w-md">
                            Đề thi Chuyên Tin
                        </h3>
                        <p id="pdf-modal-sub" class="text-[10px] text-slate-400 truncate">Trường THPT Chuyên</p>
                    </div>
                </div>

                <!-- Center: Mode Tabs (PDF / Split / Solutions) -->
                <div class="flex items-center bg-slate-900 p-0.5 rounded-lg border border-slate-800">
                    <button onclick="setModalViewMode('pdf')" id="tab-btn-pdf" class="px-2.5 py-1 rounded-md text-2xs font-semibold text-white bg-indigo-600 transition flex items-center gap-1">
                        <i class="fa-solid fa-file-pdf"></i>
                        <span class="hidden sm:inline">Đề Thi PDF</span>
                    </button>
                    <button onclick="setModalViewMode('split')" id="tab-btn-split" class="hidden md:flex px-2.5 py-1 rounded-md text-2xs font-semibold text-slate-400 hover:text-white transition items-center gap-1">
                        <i class="fa-solid fa-columns"></i>
                        <span>Chia Đôi (Split)</span>
                    </button>
                    <button onclick="setModalViewMode('solutions')" id="tab-btn-solutions" class="px-2.5 py-1 rounded-md text-2xs font-semibold text-slate-400 hover:text-white transition flex items-center gap-1">
                        <i class="fa-solid fa-code"></i>
                        <span>Lời Giải Python (<span id="tab-solutions-count">0</span>)</span>
                    </button>
                </div>

                <!-- Right: Action Buttons -->
                <div class="flex items-center gap-1.5 shrink-0">
                    <button onclick="toggleModalFullscreen()" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700 text-2xs font-medium transition" title="Toàn màn hình">
                        <i id="fullscreen-icon" class="fa-solid fa-expand text-2xs"></i>
                        <span class="hidden xl:inline" id="fullscreen-text">Toàn màn hình</span>
                    </button>
                    <a id="pdf-modal-download" href="#" download class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700 text-2xs font-medium transition" title="Tải file PDF về máy">
                        <i class="fa-solid fa-download text-2xs"></i>
                        <span class="hidden xl:inline">Tải PDF</span>
                    </a>
                    <a id="pdf-modal-newtab" href="#" target="_blank" class="inline-flex items-center gap-1 px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700 text-2xs font-medium transition" title="Mở tab mới">
                        <i class="fa-solid fa-arrow-up-right-from-square text-2xs"></i>
                        <span class="hidden xl:inline">Tab mới</span>
                    </a>
                    <button onclick="closePdfModal()" class="w-6 h-6 rounded bg-slate-800 hover:bg-red-600 hover:text-white text-slate-400 flex items-center justify-center transition" title="Đóng (Esc)">
                        <i class="fa-solid fa-xmark text-sm"></i>
                    </button>
                </div>
            </div>

            <!-- Modal Content Area (Supports PDF / Solutions / Split View) -->
            <div class="flex-1 bg-slate-950 relative overflow-hidden flex flex-row">
                
                <!-- Left Pane: PDF Viewer -->
                <div id="modal-pane-pdf" class="flex-1 h-full relative overflow-hidden flex flex-col">
                    <div id="pdf-loading" class="absolute inset-0 flex flex-col items-center justify-center gap-2 bg-slate-950 text-slate-400 z-10">
                        <i class="fa-solid fa-circle-notch fa-spin text-2xl text-indigo-500"></i>
                        <span class="text-2xs font-medium">Đang tải đề thi PDF...</span>
                    </div>
                    <iframe id="pdf-frame" src="" class="w-full h-full flex-1 border-0" onload="document.getElementById('pdf-loading').classList.add('hidden')"></iframe>
                </div>

                <!-- Right Pane: Solutions & Discussion -->
                <div id="modal-pane-solutions" class="hidden flex-1 h-full bg-slate-900 border-l border-slate-800 flex flex-col overflow-hidden">
                    
                    <!-- Solutions Sub-Header -->
                    <div class="p-3 border-b border-slate-800 bg-slate-950/60 flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <span class="font-bold text-xs text-white">Đóng góp lời giải & Code</span>
                            <span id="solution-badge-total" class="px-1.5 py-0.5 rounded bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 text-[10px] font-semibold">0 bài</span>
                        </div>
                        <button onclick="openAddSolutionForm()" class="px-2.5 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-2xs transition flex items-center gap-1 shadow-sm">
                            <i class="fa-solid fa-plus text-[10px]"></i>
                            <span>Nộp code mới</span>
                        </button>
                    </div>

                    <!-- Solutions Container: List or Form -->
                    <div class="flex-1 overflow-y-auto p-3 space-y-3 custom-scrollbar" id="solutions-content-area">
                        <!-- Dynamic solutions list or submit form injected by JS -->
                    </div>

                </div>

            </div>
        </div>
    </div>

    <!-- Supabase Settings Modal -->
    <div id="config-modal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-3 bg-slate-950/80 backdrop-blur-sm">
        <div class="bg-slate-900 border border-slate-700 rounded-xl w-full max-w-md p-4 shadow-2xl space-y-3">
            <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <div class="w-7 h-7 rounded bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center">
                        <i class="fa-solid fa-cloud text-xs"></i>
                    </div>
                    <h3 class="font-bold text-xs text-white">Cấu hình Cloud Database (Supabase)</h3>
                </div>
                <button onclick="closeConfigModal()" class="text-slate-400 hover:text-white"><i class="fa-solid fa-xmark"></i></button>
            </div>
            
            <p class="text-2xs text-slate-400">
                Để học sinh khắp nơi cùng chia sẻ và xem code Python trực tiếp, hãy kết nối dự án Supabase miễn phí của bạn. Nếu để trống, dữ liệu sẽ lưu tạm vào trình duyệt (LocalStorage).
            </p>

            <div class="space-y-2 text-xs">
                <div>
                    <label class="block text-2xs text-slate-300 font-semibold mb-1">Project URL:</label>
                    <input type="text" id="cfg-supabase-url" placeholder="https://xyzcompany.supabase.co" class="w-full px-2.5 py-1.5 rounded bg-slate-950 border border-slate-700 text-xs text-white focus:outline-none focus:ring-1 focus:ring-indigo-500">
                </div>
                <div>
                    <label class="block text-2xs text-slate-300 font-semibold mb-1">Anon Public API Key:</label>
                    <input type="password" id="cfg-supabase-key" placeholder="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." class="w-full px-2.5 py-1.5 rounded bg-slate-950 border border-slate-700 text-xs text-white focus:outline-none focus:ring-1 focus:ring-indigo-500">
                </div>
            </div>

            <div class="flex items-center justify-between pt-2 border-t border-slate-800">
                <a href="https://supabase.com" target="_blank" class="text-2xs text-indigo-400 hover:underline inline-flex items-center gap-1">
                    <span>Tạo tài khoản Supabase Free</span>
                    <i class="fa-solid fa-arrow-up-right-from-square text-[9px]"></i>
                </a>
                <div class="flex items-center gap-2">
                    <button onclick="closeConfigModal()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-2xs font-semibold transition">Hủy</button>
                    <button onclick="saveSupabaseConfig()" class="px-3 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white text-2xs font-semibold transition">Lưu kết nối</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="border-t border-slate-800/80 py-2.5 mt-3 bg-slate-950 text-center text-2xs text-slate-500">
        <p>Tổng hợp Đề thi Tuyển sinh Lớp 10 Chuyên Tin học & Kho Lời giải Python (2019 - 2026)</p>
    </footer>

    <!-- Script Data & Logic -->
    <script>
        const EXAMS_DATA = {json_data};

        let state = {{
            filtered: [...EXAMS_DATA],
            search: '',
            province: '',
            year: '',
            sortCol: 'year',
            sortAsc: false,
            page: 1,
            pageSize: 50,
            currentExam: null,
            viewMode: 'split', // 'pdf', 'split', 'solutions'
            solutionsMap: {{}} // exam_id -> array of solutions
        }};

        let supabaseClient = null;

        document.addEventListener('DOMContentLoaded', () => {{
            initSupabase();
            populateFilters();
            updateStats();
            applyFilters();
            setupEventListeners();
            loadAllSolutionsCount();
        }});

        const DEFAULT_SUPABASE_URL = "https://hlaoffzalogrybprbvrr.supabase.co";
        const DEFAULT_SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsYW9mZnphbG9ncnlicHJidnJyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTEwMjQyMDYsImV4cCI6MjEwNjYwMDIwNn0.kLuhercJOYnUgmQFoEF9NiRLJIe5g-bK-CgfF1U2gRU";

        // --- Supabase / Storage Initialization ---
        function initSupabase() {{
            const storedUrl = localStorage.getItem('supabase_url');
            const storedKey = localStorage.getItem('supabase_anon_key');

            const url = (storedUrl && storedUrl.startsWith('http')) ? storedUrl : (window.SUPABASE_CONFIG && window.SUPABASE_CONFIG.url) || DEFAULT_SUPABASE_URL;
            const key = (storedKey && storedKey.length > 20) ? storedKey : (window.SUPABASE_CONFIG && window.SUPABASE_CONFIG.anonKey) || DEFAULT_SUPABASE_ANON_KEY;

            const statusDot = document.getElementById('db-status-dot');
            const statusText = document.getElementById('db-status-text');

            if (url && key && window.supabase) {{
                try {{
                    supabaseClient = window.supabase.createClient(url, key);
                    statusDot.className = 'w-2 h-2 rounded-full bg-emerald-400';
                    statusText.textContent = 'Database: Supabase Cloud';
                }} catch (e) {{
                    console.error('Supabase init error:', e);
                    statusDot.className = 'w-2 h-2 rounded-full bg-amber-400';
                    statusText.textContent = 'Database: Offline (Local)';
                }}
            }} else {{
                statusDot.className = 'w-2 h-2 rounded-full bg-amber-400';
                statusText.textContent = 'Database: Offline (Local)';
            }}
        }}

        function openConfigModal() {{
            document.getElementById('cfg-supabase-url').value = localStorage.getItem('supabase_url') || (window.SUPABASE_CONFIG ? window.SUPABASE_CONFIG.url : '') || DEFAULT_SUPABASE_URL;
            document.getElementById('cfg-supabase-key').value = localStorage.getItem('supabase_anon_key') || (window.SUPABASE_CONFIG ? window.SUPABASE_CONFIG.anonKey : '') || DEFAULT_SUPABASE_ANON_KEY;
            document.getElementById('config-modal').classList.remove('hidden');
        }}

        function closeConfigModal() {{
            document.getElementById('config-modal').classList.add('hidden');
        }}

        function saveSupabaseConfig() {{
            const url = document.getElementById('cfg-supabase-url').value.trim();
            const key = document.getElementById('cfg-supabase-key').value.trim();

            if (url) localStorage.setItem('supabase_url', url); else localStorage.removeItem('supabase_url');
            if (key) localStorage.setItem('supabase_anon_key', key); else localStorage.removeItem('supabase_anon_key');

            initSupabase();
            closeConfigModal();
            loadAllSolutionsCount();
            if (state.currentExam) {{
                loadSolutionsForExam(state.currentExam.id);
            }}
        }}

        // --- Load Solutions Count ---
        async function loadAllSolutionsCount() {{
            let countMap = {{}};

            if (supabaseClient) {{
                try {{
                    const {{ data, error }} = await supabaseClient
                        .from('exam_solutions')
                        .select('id, exam_id');
                    
                    if (!error && data) {{
                        data.forEach(s => {{
                            countMap[s.exam_id] = (countMap[s.exam_id] || 0) + 1;
                        }});
                    }}
                }} catch (e) {{
                    console.warn('Could not fetch cloud solutions count, fallback to local:', e);
                    const localSolutions = JSON.parse(localStorage.getItem('local_exam_solutions') || '[]');
                    localSolutions.forEach(s => {{
                        countMap[s.exam_id] = (countMap[s.exam_id] || 0) + 1;
                    }});
                }}
            }} else {{
                const localSolutions = JSON.parse(localStorage.getItem('local_exam_solutions') || '[]');
                localSolutions.forEach(s => {{
                    countMap[s.exam_id] = (countMap[s.exam_id] || 0) + 1;
                }});
            }}

            state.solutionsCountMap = countMap;
            const totalSolCount = Object.values(countMap).reduce((a, b) => a + b, 0);
            document.getElementById('stat-solutions').textContent = totalSolCount;

            renderTable();
        }}

        // --- Filters & Stats ---
        function populateFilters() {{
            const provinceSelect = document.getElementById('filter-province');
            const yearSelect = document.getElementById('filter-year');

            const provinces = [...new Set(EXAMS_DATA.map(e => e.province))].sort((a, b) => a.localeCompare(b, 'vi'));
            provinces.forEach(p => {{
                const count = EXAMS_DATA.filter(e => e.province === p).length;
                const opt = document.createElement('option');
                opt.value = p;
                opt.textContent = `${{p}} (${{count}})`;
                provinceSelect.appendChild(opt);
            }});

            const years = [...new Set(EXAMS_DATA.map(e => e.year))].sort((a, b) => b.localeCompare(a));
            years.forEach(y => {{
                const count = EXAMS_DATA.filter(e => e.year === y).length;
                const opt = document.createElement('option');
                opt.value = y;
                opt.textContent = `${{y}} (${{count}})`;
                yearSelect.appendChild(opt);
            }});
        }}

        function updateStats() {{
            const total = EXAMS_DATA.length;
            const pdfCount = EXAMS_DATA.filter(e => e.has_pdf).length;
            document.getElementById('stat-total').textContent = total;
            document.getElementById('stat-pdf').textContent = pdfCount;
            document.getElementById('stat-pdf-percent').textContent = `${{Math.round((pdfCount / total) * 100)}}%`;
        }}

        function setupEventListeners() {{
            const searchInput = document.getElementById('search-input');
            const clearBtn = document.getElementById('clear-search');

            searchInput.addEventListener('input', (e) => {{
                state.search = e.target.value.trim().toLowerCase();
                state.page = 1;
                clearBtn.classList.toggle('hidden', state.search === '');
                applyFilters();
            }});

            clearBtn.addEventListener('click', () => {{
                searchInput.value = '';
                state.search = '';
                state.page = 1;
                clearBtn.classList.add('hidden');
                applyFilters();
                searchInput.focus();
            }});

            document.getElementById('filter-province').addEventListener('change', (e) => {{
                state.province = e.target.value;
                state.page = 1;
                applyFilters();
            }});

            document.getElementById('filter-year').addEventListener('change', (e) => {{
                state.year = e.target.value;
                state.page = 1;
                applyFilters();
            }});

            document.getElementById('btn-reset-filters').addEventListener('click', resetFilters);

            document.getElementById('page-size').addEventListener('change', (e) => {{
                state.pageSize = parseInt(e.target.value);
                state.page = 1;
                renderTable();
            }});

            document.addEventListener('keydown', (e) => {{
                if (e.key === 'Escape') {{
                    closePdfModal();
                    closeConfigModal();
                }}
            }});

            document.getElementById('pdf-modal').addEventListener('click', (e) => {{
                if (e.target.id === 'pdf-modal') {{
                    closePdfModal();
                }}
            }});
        }}

        function resetFilters() {{
            document.getElementById('search-input').value = '';
            document.getElementById('filter-province').value = '';
            document.getElementById('filter-year').value = '';
            document.getElementById('clear-search').classList.add('hidden');
            state.search = '';
            state.province = '';
            state.year = '';
            state.page = 1;
            applyFilters();
        }}

        function applyFilters() {{
            state.filtered = EXAMS_DATA.filter(item => {{
                if (state.province && item.province !== state.province) return false;
                if (state.year && item.year !== state.year) return false;
                if (state.search) {{
                    const s = state.search;
                    const matchProv = item.province.toLowerCase().includes(s);
                    const matchSchool = item.school.toLowerCase().includes(s);
                    const matchYear = item.year.toLowerCase().includes(s);
                    const matchTitle = item.title.toLowerCase().includes(s);
                    if (!matchProv && !matchSchool && !matchYear && !matchTitle) return false;
                }}
                return true;
            }});

            sortData();
            renderTable();
        }}

        function handleSort(col) {{
            if (state.sortCol === col) {{
                state.sortAsc = !state.sortAsc;
            }} else {{
                state.sortCol = col;
                state.sortAsc = true;
            }}
            sortData();
            updateSortUI();
            renderTable();
        }}

        function sortData() {{
            const col = state.sortCol;
            const asc = state.sortAsc ? 1 : -1;

            state.filtered.sort((a, b) => {{
                if (col === 'id') return (a.id - b.id) * asc;
                if (col === 'has_pdf') return ((a.has_pdf === b.has_pdf) ? 0 : a.has_pdf ? -1 : 1) * asc;
                
                let valA = a[col] || '';
                let valB = b[col] || '';

                if (col === 'province' || col === 'school' || col === 'title') {{
                    return valA.localeCompare(valB, 'vi') * asc;
                }}
                if (col === 'year') {{
                    return valA.localeCompare(valB) * asc;
                }}
                return 0;
            }});
        }}

        function updateSortUI() {{
            document.querySelectorAll('.sort-icon').forEach(el => {{
                el.textContent = '';
            }});

            const activeIcon = document.querySelector(`.sort-icon[data-col="${{state.sortCol}}"]`);
            if (activeIcon) {{
                activeIcon.textContent = state.sortAsc ? '▲' : '▼';
            }}

            const labels = {{
                'province': 'Tên Tỉnh',
                'school': 'Tên Trường',
                'year': 'Năm Học',
                'id': 'Số thứ tự',
                'has_pdf': 'Trạng thái PDF'
            }};
            let dir = state.sortAsc ? '(A → Z)' : '(Z → A)';
            if (state.sortCol === 'year') {{
                dir = state.sortAsc ? '(Cũ → Mới)' : '(Mới nhất)';
            }}
            if (state.sortCol === 'id') {{
                dir = state.sortAsc ? '(Tăng dần)' : '(Giảm dần)';
            }}
            document.getElementById('current-sort-label').textContent = `${{labels[state.sortCol] || state.sortCol}} ${{dir}}`;
        }}

        function renderTable() {{
            const tbody = document.getElementById('exam-table-body');
            const emptyState = document.getElementById('empty-state');
            const totalLabel = document.getElementById('total-count-label');
            const filteredCount = document.getElementById('filtered-count');

            filteredCount.textContent = state.filtered.length;
            totalLabel.textContent = `/ ${{EXAMS_DATA.length}} đề`;

            if (state.filtered.length === 0) {{
                tbody.innerHTML = '';
                emptyState.classList.remove('hidden');
                document.getElementById('pagination-controls').innerHTML = '';
                return;
            }}

            emptyState.classList.add('hidden');

            const totalPages = Math.ceil(state.filtered.length / state.pageSize);
            if (state.page > totalPages) state.page = totalPages;
            if (state.page < 1) state.page = 1;

            const startIdx = (state.page - 1) * state.pageSize;
            const endIdx = startIdx + state.pageSize;
            const pageItems = state.filtered.slice(startIdx, endIdx);

            tbody.innerHTML = pageItems.map((item, idx) => {{
                const globalIdx = startIdx + idx + 1;
                const solCount = (state.solutionsCountMap && state.solutionsCountMap[item.id]) || 0;
                
                let pdfBadge = '';
                if (item.has_pdf) {{
                    const solBadge = solCount > 0 
                        ? `<span class="px-1.5 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 text-[10px] font-bold border border-cyan-400/30">${{solCount}} bài giải</span>` 
                        : '';

                    pdfBadge = `
                        <div class="inline-flex items-center gap-1.5">
                            <button onclick="openPdfModal('${{encodeURIComponent(JSON.stringify(item))}}', 'split')" 
                                class="inline-flex items-center gap-1.5 px-3 py-1 rounded bg-indigo-600/20 hover:bg-indigo-600 text-indigo-300 hover:text-white border border-indigo-500/30 text-2xs font-semibold transition whitespace-nowrap shadow-sm" title="Xem đề thi PDF và cột bình luận lời giải kiểu Facebook">
                                <i class="fa-solid fa-columns text-2xs"></i>
                                <span>Xem đề & Lời giải</span>
                                ${{solBadge}}
                            </button>
                            <a href="${{item.pdf_url}}" download class="p-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 text-2xs transition" title="Tải file PDF về máy">
                                <i class="fa-solid fa-download text-2xs"></i>
                            </a>
                        </div>
                    `;
                }} else {{
                    pdfBadge = `<span class="inline-flex items-center px-2 py-0.5 rounded bg-slate-800/80 text-slate-500 text-2xs">Chưa tải</span>`;
                }}

                return `
                    <tr class="hover:bg-slate-800/40 transition-colors group">
                        <td class="py-2 px-2 text-center font-mono text-2xs text-slate-500">${{globalIdx}}</td>
                        <td class="py-2 px-2.5 font-semibold text-white whitespace-nowrap group-hover:text-indigo-300 transition-colors">
                            ${{item.province}}
                        </td>
                        <td class="py-2 px-2.5 text-slate-200">
                            ${{item.school}}
                        </td>
                        <td class="py-2 px-2 text-center whitespace-nowrap">
                            <span class="inline-flex items-center px-2 py-0.5 rounded bg-slate-800 text-slate-300 font-mono text-2xs border border-slate-700/60 font-medium">
                                ${{item.year}}
                            </span>
                        </td>
                        <td class="py-2 px-2.5">
                            <a href="${{item.original_url}}" target="_blank" rel="noopener noreferrer" 
                               class="text-indigo-400 hover:text-indigo-300 hover:underline inline-flex items-center gap-1 text-2xs font-medium" title="${{item.title}}">
                                <span>${{item.title}}</span>
                                <i class="fa-solid fa-arrow-up-right-from-square text-[9px] opacity-70"></i>
                            </a>
                        </td>
                        <td class="py-2 px-2.5 text-center whitespace-nowrap">
                            ${{pdfBadge}}
                        </td>
                    </tr>
                `;
            }}).join('');

            renderPagination(totalPages);
        }}

        function renderPagination(totalPages) {{
            const container = document.getElementById('pagination-controls');
            if (totalPages <= 1) {{
                container.innerHTML = '';
                return;
            }}

            let html = '';
            
            html += `
                <button onclick="changePage(${{state.page - 1}})" ${{state.page === 1 ? 'disabled class="opacity-30 cursor-not-allowed"' : 'class="hover:bg-slate-800"'}} 
                    class="px-2 py-1 rounded border border-slate-700 text-slate-300 text-2xs transition">
                    <i class="fa-solid fa-chevron-left text-[9px]"></i>
                </button>
            `;

            for (let i = 1; i <= totalPages; i++) {{
                if (i === 1 || i === totalPages || (i >= state.page - 1 && i <= state.page + 1)) {{
                    const activeClass = i === state.page ? 'bg-indigo-600 text-white border-indigo-500 font-bold' : 'hover:bg-slate-800 text-slate-300 border-slate-700';
                    html += `
                        <button onclick="changePage(${{i}})" class="px-2.5 py-1 rounded border text-2xs transition ${{activeClass}}">
                            ${{i}}
                        </button>
                    `;
                }} else if (i === state.page - 2 || i === state.page + 2) {{
                    html += `<span class="px-1 text-slate-600 text-2xs">...</span>`;
                }}
            }}

            html += `
                <button onclick="changePage(${{state.page + 1}})" ${{state.page === totalPages ? 'disabled class="opacity-30 cursor-not-allowed"' : 'class="hover:bg-slate-800"'}} 
                    class="px-2 py-1 rounded border border-slate-700 text-slate-300 text-2xs transition">
                    <i class="fa-solid fa-chevron-right text-[9px]"></i>
                </button>
            `;

            container.innerHTML = html;
        }}

        function changePage(page) {{
            state.page = page;
            renderTable();
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        // --- Modal & View Modes ---
        let isFullscreen = false;
        function toggleModalFullscreen() {{
            const card = document.getElementById('pdf-modal-card');
            const icon = document.getElementById('fullscreen-icon');
            const text = document.getElementById('fullscreen-text');
            
            isFullscreen = !isFullscreen;
            if (isFullscreen) {{
                card.classList.remove('rounded-md', 'max-w-[99.5vw]', 'max-h-[99vh]');
                card.classList.add('rounded-none', 'w-screen', 'h-screen', 'fixed', 'inset-0');
                icon.className = 'fa-solid fa-compress text-2xs';
                text.textContent = 'Thu nhỏ';
            }} else {{
                card.classList.remove('rounded-none', 'w-screen', 'h-screen', 'fixed', 'inset-0');
                card.classList.add('rounded-md', 'max-w-[99.5vw]', 'max-h-[99vh]');
                icon.className = 'fa-solid fa-expand text-2xs';
                text.textContent = 'Toàn màn hình';
            }}
        }}

        function setModalViewMode(mode) {{
            state.viewMode = mode;
            const pdfPane = document.getElementById('modal-pane-pdf');
            const solPane = document.getElementById('modal-pane-solutions');
            const btnPdf = document.getElementById('tab-btn-pdf');
            const btnSplit = document.getElementById('tab-btn-split');
            const btnSol = document.getElementById('tab-btn-solutions');

            [btnPdf, btnSplit, btnSol].forEach(b => {{
                b.className = 'px-2.5 py-1 rounded-md text-2xs font-semibold text-slate-400 hover:text-white transition flex items-center gap-1';
            }});

            if (mode === 'pdf') {{
                pdfPane.classList.remove('hidden');
                pdfPane.className = 'flex-1 h-full relative overflow-hidden flex flex-col';
                solPane.classList.add('hidden');
                btnPdf.className = 'px-2.5 py-1 rounded-md text-2xs font-semibold text-white bg-indigo-600 transition flex items-center gap-1';
            }} else if (mode === 'split') {{
                pdfPane.classList.remove('hidden');
                pdfPane.className = 'w-full md:w-[60%] lg:w-[62%] h-full relative overflow-hidden flex flex-col border-r border-slate-800';
                solPane.classList.remove('hidden');
                solPane.className = 'w-full md:w-[40%] lg:w-[38%] h-full bg-slate-900 flex flex-col overflow-hidden';
                btnSplit.className = 'px-2.5 py-1 rounded-md text-2xs font-semibold text-white bg-indigo-600 transition flex items-center gap-1';
            }} else if (mode === 'solutions') {{
                pdfPane.classList.add('hidden');
                solPane.classList.remove('hidden');
                solPane.className = 'flex-1 h-full bg-slate-900 flex flex-col overflow-hidden';
                btnSol.className = 'px-2.5 py-1 rounded-md text-2xs font-semibold text-white bg-cyan-600 transition flex items-center gap-1';
            }}
        }}

        function openPdfModal(encodedItem, initialMode = 'split') {{
            const item = JSON.parse(decodeURIComponent(encodedItem));
            state.currentExam = item;

            const modal = document.getElementById('pdf-modal');
            const frame = document.getElementById('pdf-frame');
            const title = document.getElementById('pdf-modal-title');
            const sub = document.getElementById('pdf-modal-sub');
            const downloadBtn = document.getElementById('pdf-modal-download');
            const newtabBtn = document.getElementById('pdf-modal-newtab');
            const loading = document.getElementById('pdf-loading');

            title.textContent = item.title;
            sub.textContent = `${{item.province}} • ${{item.school}} • Năm học ${{item.year}}`;
            downloadBtn.href = item.pdf_url;
            downloadBtn.setAttribute('download', item.pdf_name || 'de_thi.pdf');
            newtabBtn.href = item.pdf_url;

            loading.classList.remove('hidden');
            frame.src = `${{item.pdf_url}}#toolbar=1&navpanes=0&scrollbar=1&view=FitH`;

            setModalViewMode(initialMode);
            loadSolutionsForExam(item.id);

            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }}

        function closePdfModal() {{
            const modal = document.getElementById('pdf-modal');
            const frame = document.getElementById('pdf-frame');
            modal.classList.add('hidden');
            frame.src = '';
            document.body.style.overflow = 'auto';
            if (isFullscreen) {{
                toggleModalFullscreen();
            }}
        }}

        // --- Solutions CRUD & Render Logic ---
        async function loadSolutionsForExam(examId) {{
            const area = document.getElementById('solutions-content-area');
            area.innerHTML = `
                <div class="py-12 text-center text-slate-500">
                    <i class="fa-solid fa-circle-notch fa-spin text-xl text-indigo-500 mb-2"></i>
                    <p class="text-2xs">Đang tải danh sách lời giải...</p>
                </div>
            `;

            let solutions = [];

            if (supabaseClient) {{
                try {{
                    const {{ data, error }} = await supabaseClient
                        .from('exam_solutions')
                        .select('*')
                        .eq('exam_id', examId)
                        .order('created_at', {{ ascending: false }});

                    if (!error && data) {{
                        solutions = data;
                    }} else {{
                        const allLocal = JSON.parse(localStorage.getItem('local_exam_solutions') || '[]');
                        solutions = allLocal.filter(s => s.exam_id === examId);
                    }}
                }} catch (e) {{
                    console.warn('Could not fetch from Supabase, using local:', e);
                    const allLocal = JSON.parse(localStorage.getItem('local_exam_solutions') || '[]');
                    solutions = allLocal.filter(s => s.exam_id === examId);
                }}
            }} else {{
                const allLocal = JSON.parse(localStorage.getItem('local_exam_solutions') || '[]');
                solutions = allLocal.filter(s => s.exam_id === examId);
            }}

            state.solutionsMap[examId] = solutions;
            
            // Update badges
            document.getElementById('tab-solutions-count').textContent = solutions.length;
            document.getElementById('solution-badge-total').textContent = `${{solutions.length}} bài`;

            renderSolutionsList(solutions);
        }}

        function renderSolutionsList(solutions) {{
            const area = document.getElementById('solutions-content-area');

            if (!solutions || solutions.length === 0) {{
                area.innerHTML = `
                    <div class="py-12 text-center space-y-2">
                        <div class="w-10 h-10 rounded-full bg-slate-800 text-slate-500 flex items-center justify-center mx-auto text-sm">
                            <i class="fa-solid fa-code"></i>
                        </div>
                        <h4 class="text-xs font-semibold text-slate-300">Chưa có bài giải nào cho đề này</h4>
                        <p class="text-2xs text-slate-500 max-w-xs mx-auto">Hãy là người đầu tiên chia sẻ code Python giải các bài trong đề thi này!</p>
                        <button onclick="openAddSolutionForm()" class="mt-2 px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-2xs font-semibold transition">
                            <i class="fa-solid fa-plus mr-1"></i> Viết lời giải đầu tiên
                        </button>
                    </div>
                `;
                return;
            }}

            let html = solutions.map((sol, idx) => {{
                const dateStr = sol.created_at ? new Date(sol.created_at).toLocaleDateString('vi-VN', {{ day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit' }}) : 'Vừa xong';
                const escapedCode = sol.code.replace(/</g, '&lt;').replace(/>/g, '&gt;');
                const author = sol.author || 'Ẩn danh';
                const prob = sol.problem_name || 'Bài giải';

                return `
                    <div class="bg-slate-950/80 border border-slate-800 rounded-lg p-3 space-y-2.5 shadow-sm">
                        <!-- Card Header -->
                        <div class="flex items-center justify-between border-b border-slate-800/80 pb-2">
                            <div class="flex items-center gap-2">
                                <div class="w-7 h-7 rounded-full bg-indigo-500/20 text-indigo-300 font-bold flex items-center justify-center text-2xs ring-1 ring-indigo-500/30">
                                    ${{author.charAt(0).toUpperCase()}}
                                </div>
                                <div>
                                    <div class="font-bold text-xs text-white flex items-center gap-1.5">
                                        <span>${{author}}</span>
                                        <span class="px-1.5 py-0.2 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 text-[10px] font-semibold">${{prob}}</span>
                                    </div>
                                    <span class="text-[10px] text-slate-500 font-mono">${{dateStr}}</span>
                                </div>
                            </div>
                        </div>

                        <!-- Explanation (if any) -->
                        ${{sol.explanation ? `
                            <div class="text-2xs text-slate-300 bg-slate-900/90 rounded p-2 border border-slate-800/80 leading-relaxed">
                                <span class="font-semibold text-slate-400 block mb-0.5"><i class="fa-regular fa-lightbulb text-amber-400 mr-1"></i>Ý tưởng giải:</span>
                                ${{sol.explanation.replace(/\\n/g, '<br>')}}
                            </div>
                        ` : ''}}

                        <!-- Code Block with Spoiler Hide/Reveal -->
                        <div id="spoiler-container-${{idx}}" class="mt-2">
                            <!-- Spoiler Cover (Default Hidden State) -->
                            <div id="spoiler-cover-${{idx}}" onclick="toggleCodeSpoiler(${{idx}})" 
                                class="p-3 rounded-lg border border-slate-700/80 bg-slate-900/90 hover:bg-slate-800/90 hover:border-cyan-500/40 transition cursor-pointer flex flex-col items-center justify-center gap-1 group select-none shadow-sm">
                                <div class="flex items-center gap-1.5 text-cyan-400 group-hover:text-cyan-300 font-bold text-xs">
                                    <i class="fa-solid fa-eye text-xs"></i>
                                    <span>Bấm vào để xem code lời giải Python</span>
                                </div>
                                <p class="text-[10px] text-slate-400">Code đang ẩn để bạn tự suy nghĩ trước khi xem lời giải</p>
                            </div>

                            <!-- Revealed Code (Hidden by default) -->
                            <div id="spoiler-content-${{idx}}" class="hidden space-y-1.5 animate-in fade-in zoom-in-95 duration-150">
                                <div class="flex items-center justify-between px-1 text-[11px]">
                                    <span class="text-slate-400 font-mono text-[10px] flex items-center gap-1"><i class="fa-brands fa-python text-emerald-400"></i> Python 3</span>
                                    <div class="flex items-center gap-1">
                                        <button onclick="copySolutionCode('code-block-${{idx}}', this)" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-[10px] font-medium transition flex items-center gap-1" title="Sao chép code">
                                            <i class="fa-solid fa-copy text-[9px]"></i>
                                            <span>Copy Code</span>
                                        </button>
                                        <button onclick="toggleCodeSpoiler(${{idx}})" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white text-[10px] font-medium transition flex items-center gap-1" title="Ẩn lại code">
                                            <i class="fa-solid fa-eye-slash text-[9px]"></i>
                                            <span>Ẩn code</span>
                                        </button>
                                    </div>
                                </div>
                                <pre><code id="code-block-${{idx}}" class="language-python font-mono">${{escapedCode}}</code></pre>
                            </div>
                        </div>
                    </div>
                `;
            }}).join('');

            area.innerHTML = html;

            // Trigger Highlight.js
            document.querySelectorAll('#solutions-content-area pre code').forEach((el) => {{
                hljs.highlightElement(el);
            }});
        }}

        function openAddSolutionForm() {{
            const area = document.getElementById('solutions-content-area');
            const savedAuthor = localStorage.getItem('last_author_name') || '';

            area.innerHTML = `
                <div class="bg-slate-950/90 border border-slate-800 rounded-lg p-3.5 space-y-3">
                    <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                        <h4 class="font-bold text-xs text-white flex items-center gap-1.5">
                            <i class="fa-solid fa-code text-cyan-400"></i>
                            <span>Đóng góp bài giải Python</span>
                        </h4>
                        <button onclick="loadSolutionsForExam(state.currentExam.id)" class="text-slate-400 hover:text-white text-xs">
                            <i class="fa-solid fa-arrow-left mr-1"></i> Quay lại
                        </button>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
                        <div>
                            <label class="block text-2xs text-slate-300 font-semibold mb-1">Tên của bạn / Nickname: <span class="text-red-400">*</span></label>
                            <input type="text" id="sol-author" value="${{savedAuthor}}" placeholder="Ví dụ: Nguyễn Văn A (Lớp 10 Tin)" 
                                class="w-full px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                        </div>
                        <div>
                            <label class="block text-2xs text-slate-300 font-semibold mb-1">Tên bài trong đề: <span class="text-red-400">*</span></label>
                            <input type="text" id="sol-problem" placeholder="Ví dụ: Bài 1 - Tổng ước, Bài 2 - Xâu con..." 
                                class="w-full px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                        </div>
                    </div>

                    <div>
                        <label class="block text-2xs text-slate-300 font-semibold mb-1">Giải thích thuật toán / Ý tưởng giải (tùy chọn):</label>
                        <textarea id="sol-explanation" rows="2" placeholder="Ví dụ: Dùng thuật toán sàng nguyên tố hoặc quy hoạch động với độ phức tạp O(N)..." 
                            class="w-full px-2.5 py-1.5 rounded bg-slate-900 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-1 focus:ring-indigo-500"></textarea>
                    </div>

                    <div>
                        <div class="flex items-center justify-between mb-1">
                            <label class="text-2xs text-slate-300 font-semibold">Mã nguồn Python 3: <span class="text-red-400">*</span></label>
                            <span class="text-[10px] text-slate-500">Hỗ trợ phím Tab thụt 4 spaces</span>
                        </div>
                        <textarea id="sol-code" rows="10" placeholder="import sys\\n\\ndef solve():\\n    # Viết code của bạn ở đây...\\n    pass\\n\\nif __name__ == '__main__':\\n    solve()" 
                            class="w-full px-3 py-2 rounded bg-slate-900 border border-slate-700 text-xs text-cyan-300 font-mono focus:outline-none focus:ring-1 focus:ring-cyan-500 leading-relaxed custom-scrollbar"></textarea>
                    </div>

                    <div class="flex items-center justify-between pt-2 border-t border-slate-800">
                        <button onclick="loadSolutionsForExam(state.currentExam.id)" class="px-3 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-2xs font-semibold transition">
                            Hủy bỏ
                        </button>
                        <button onclick="submitSolution()" id="btn-submit-solution" class="px-4 py-1.5 rounded bg-indigo-600 hover:bg-indigo-500 text-white text-2xs font-bold transition flex items-center gap-1.5 shadow-md shadow-indigo-600/20">
                            <i class="fa-solid fa-paper-plane text-2xs"></i>
                            <span>Gửi bài giải</span>
                        </button>
                    </div>
                </div>
            `;

            // Enable Tab key inside textarea
            const codeArea = document.getElementById('sol-code');
            codeArea.addEventListener('keydown', function(e) {{
                if (e.key === 'Tab') {{
                    e.preventDefault();
                    const start = this.selectionStart;
                    const end = this.selectionEnd;
                    this.value = this.value.substring(0, start) + "    " + this.value.substring(end);
                    this.selectionStart = this.selectionEnd = start + 4;
                }}
            }});
        }}

        async function submitSolution() {{
            const authorInput = document.getElementById('sol-author');
            const problemInput = document.getElementById('sol-problem');
            const expInput = document.getElementById('sol-explanation');
            const codeInput = document.getElementById('sol-code');
            const submitBtn = document.getElementById('btn-submit-solution');

            const author = authorInput.value.trim();
            const problem = problemInput.value.trim();
            const explanation = expInput.value.trim();
            const code = codeInput.value.trim();

            if (!author) {{
                alert('Vui lòng nhập tên của bạn hoặc nickname!');
                authorInput.focus();
                return;
            }}
            if (!problem) {{
                alert('Vui lòng nhập tên bài toán (Ví dụ: Bài 1 - Tổng ước)!');
                problemInput.focus();
                return;
            }}
            if (!code || code.length < 5) {{
                alert('Vui lòng nhập mã nguồn code Python!');
                codeInput.focus();
                return;
            }}

            localStorage.setItem('last_author_name', author);
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-circle-notch fa-spin"></i> Đang gửi...';

            const newSolution = {{
                exam_id: state.currentExam.id,
                exam_title: state.currentExam.title,
                problem_name: problem,
                author: author,
                language: 'python',
                code: code,
                explanation: explanation,
                created_at: new Date().toISOString()
            }};

            let savedToCloud = false;

            if (supabaseClient) {{
                try {{
                    const {{ data, error }} = await supabaseClient
                        .from('exam_solutions')
                        .insert([newSolution]);
                    
                    if (!error) {{
                        savedToCloud = true;
                    }} else {{
                        console.error('Supabase insert error:', error);
                    }}
                }} catch (e) {{
                    console.error('Cloud submission error:', e);
                }}
            }}

            // Always save locally as well
            const allLocal = JSON.parse(localStorage.getItem('local_exam_solutions') || '[]');
            allLocal.unshift(newSolution);
            localStorage.setItem('local_exam_solutions', JSON.stringify(allLocal));

            loadAllSolutionsCount();
            loadSolutionsForExam(state.currentExam.id);
        }}

        function copySolutionCode(codeId, btn) {{
            const codeEl = document.getElementById(codeId);
            if (!codeEl) return;

            navigator.clipboard.writeText(codeEl.innerText).then(() => {{
                const originalHtml = btn.innerHTML;
                btn.innerHTML = '<i class="fa-solid fa-check text-emerald-400"></i> <span class="text-emerald-400">Đã chép!</span>';
                setTimeout(() => {{
                    btn.innerHTML = originalHtml;
                }}, 2000);
            }}).catch(err => {{
                console.error('Copy failed:', err);
            }});
        }}

        function toggleCodeSpoiler(idx) {{
            const cover = document.getElementById(`spoiler-cover-${{idx}}`);
            const content = document.getElementById(`spoiler-content-${{idx}}`);
            if (!cover || !content) return;
            if (content.classList.contains('hidden')) {{
                content.classList.remove('hidden');
                cover.classList.add('hidden');
            }} else {{
                content.classList.add('hidden');
                cover.classList.remove('hidden');
            }}
        }}
    </script>
</body>
</html>
"""
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated clean & compact responsive HTML page: {out_path}")

def main():
    md_path = 'e:/DeThiChuyenTin/DanhSach_DeThi_ChuyenTin.md'
    html_path = 'e:/DeThiChuyenTin/index.html'
    data = parse_markdown_table(md_path)
    print(f"Parsed {len(data)} exams from markdown table.")
    build_html_page(data, html_path)

if __name__ == '__main__':
    main()
